import datetime
import json
import time
from urllib.parse import urlencode

import requests

from meican.commands import get_dishes, get_restaurants, get_tabs
from meican.exceptions import MeiCanError, MeiCanLoginFail, NoOrderAvailable
from meican.models import TabStatus


class RestUrl(object):
    """用来存储 MeiCan Rest 接口的类"""

    @classmethod
    def get_base_url(cls, path, params=None, wrap=True):
        """
        :type path: str | unicode
        :type params: dict
        :type wrap: bool
        :rtype: str | unicode
        """
        if params:
            if wrap:
                params["noHttpGetCache"] = int(time.time() * 1000)
            path = "{}?{}".format(path, urlencode(sorted(params.items())))
        return "https://meican.com/{}".format(path)

    @classmethod
    def login(cls):
        return cls.get_base_url("account/directlogin")

    @classmethod
    def calender_items(cls, detail=False):
        today = datetime.date.today()
        one_week = datetime.timedelta(weeks=1)
        data = {
            "beginDate": today.strftime("%Y-%m-%d"),
            "endDate": (today + one_week).strftime("%Y-%m-%d"),
            "withOrderDetail": detail,
        }
        return cls.get_base_url("preorder/api/v2.1/calendarItems/list", data)

    @classmethod
    def restaurants(cls, tab):
        """
        :type tab: meican.models.Tab
        """
        data = {"tabUniqueId": tab.uid, "targetTime": tab.target_time}
        return cls.get_base_url("preorder/api/v2.1/restaurants/list", data)

    @classmethod
    def dishes(cls, restaurant):
        """
        :type restaurant: meican.models.Restaurant
        """
        tab = restaurant.tab
        data = {"restaurantUniqueId": restaurant.uid, "tabUniqueId": tab.uid, "targetTime": tab.target_time}
        return cls.get_base_url("preorder/api/v2.1/restaurants/show", data)

    @classmethod
    def order(cls, dish, address_uid=""):
        """
        :type dish: meican.models.Dish
        :type address_uid: str
        """
        tab = dish.restaurant.tab
        address_uid = address_uid or tab.addresses[0].uid
        data = {
            "order": json.dumps([{"count": "1", "dishId": "{}".format(dish.id)}]),
            "tabUniqueId": tab.uid,
            "targetTime": tab.target_time,
            "corpAddressUniqueId": address_uid,
            "userAddressUniqueId": address_uid,
        }
        return cls.get_base_url("preorder/api/v2.1/orders/add", data, wrap=False)


class MeiCan(object):
    def __init__(self, username, password, user_agent=None):
        """
        :type username: str | unicode
        :type password: str | unicode
        """
        self.responses = []
        self._session = requests.Session()
        user_agent = user_agent or "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        self._session.headers["User-Agent"] = user_agent
        self._calendar_items = None
        self._tabs = None

        form_data = {"username": username, "password": password, "loginType": "username", "remember": True}
        response = self._request("post", RestUrl.login(), form_data)
        if 200 != response.status_code or "用户名或密码错误" in response.text:
            raise MeiCanLoginFail("login fail because username or password incorrect")

    @property
    def tabs(self):
        """
        :rtype: list[meican.models.Tab]
        """
        if not self._tabs:
            self.load_tabs()
        return self._tabs

    @property
    def next_available_tab(self):
        """
        :rtype: meican.models.Tab
        """
        available_tabs = [_ for _ in self.tabs if _.status == TabStatus.AVAIL]
        return available_tabs[0] if available_tabs else None

    def load_tabs(self, refresh=False):
        if not self._calendar_items or refresh:
            self._calendar_items = self.http_get(RestUrl.calender_items())
            self._tabs = get_tabs(self._calendar_items)

    def get_restaurants(self, tab):
        """
        :type tab: meican.models.Tab
        :rtype: list[meican.models.Restaurant]
        """
        data = self.http_get(RestUrl.restaurants(tab))
        return get_restaurants(tab, data)

    def get_dishes(self, restaurant):
        """
        :type restaurant: meican.models.Restaurant
        """
        data = self.http_get(RestUrl.dishes(restaurant))
        return get_dishes(restaurant, data)

    def list_dishes(self, tab=None):
        """
        :type tab: meican.models.Tab
        :rtype: list[meican.models.Dish]
        """
        tab = tab or self.next_available_tab
        if not tab:
            raise NoOrderAvailable("Currently no available orders")
        restaurants = self.get_restaurants(tab)
        dishes = []
        for restaurant in restaurants:
            dishes.extend(self.get_dishes(restaurant))
        return dishes

    def order(self, dish, address_uid=""):
        """
        :type dish: meican.models.Dish
        :type address_uid: str
        """
        data = self.http_post(RestUrl.order(dish, address_uid=address_uid))
        return data

    def http_get(self, url, **kwargs):
        """
        :type url: str | unicode
        :rtype: dict | str | unicode
        """
        response = self._request("get", url, **kwargs)
        return response.json()

    def http_post(self, url, data=None, **kwargs):
        """
        :type url: str | unicode
        :type data: dict
        :rtype: dict | str | unicode
        """
        response = self._request("post", url, data, **kwargs)
        return response.json()

    def _request(self, method, url, data=None, **kwargs):
        """
        :type method: str | unicode
        :type url: str | unicode
        :type data: dict
        :type kwargs: dict
        :rtype: requests.Response
        """
        func = getattr(self._session, method)
        response = func(url, data=data, **kwargs)  # type: requests.Response
        response.encoding = response.encoding or "utf-8"
        self.responses.append(response)
        if response.status_code != 200:
            error = response.json()
            raise MeiCanError("[{}] {}".format(error.get("error", ""), error.get("error_description", "")))
        return response
