# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json
import time
from functools import reduce

import requests

from meican.commands import get_tabs_from_calendar_items
from meican.exceptions import MeiCanError
from meican.utils import join_dict
from urls import login_url, order_url, restaurant_dishes_url, restaurants_url

address_uid = 'e7b93aafd597'  # 再惠


class RestUrl(object):
    """ 用来存储 MeiCan Rest 接口的类 """

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
                params['noHttpGetCache'] = int(time.time() * 1000)
            path = '{}?{}'.format(path, join_dict(params))
        return 'https://meican.com/{}'.format(path)

    @classmethod
    def login(cls):
        return cls.get_base_url('account/directlogin')

    @classmethod
    def calender_items(cls, detail=False):
        today = datetime.date.today()
        one_week = datetime.timedelta(weeks=1)
        data = {
            'beginDate': today.strftime('%Y-%m-%d'),
            'endDate': (today + one_week).strftime('%Y-%m-%d'),
            'withOrderDetail': detail,
        }
        return cls.get_base_url('preorder/api/v2.1/calendarItems/list', data)


class MeiCan(object):
    def __init__(self):
        self._session = requests.Session()
        self.responses = []
        self._calendar_items = None
        self._tabs = None

    @classmethod
    def login(cls, username, password):
        """
        :type username: str | unicode
        :type password: str | unicode
        """
        meican = cls()
        form_data = {'username': username, 'password': password, 'loginType': 'username', 'remember': True}
        response = meican._request('post', login_url(), form_data)
        if 200 != response.status_code:  # or '用户名或密码错误' in response.content:
            raise MeiCanError('login fail because username or password incorrect')
        meican.load_tabs()
        return meican

    def load_tabs(self, refresh=False):
        if not self._calendar_items or refresh:
            self._calendar_items = self.http_get(RestUrl.calender_items())
            self._tabs = get_tabs_from_calendar_items(self._calendar_items)

    def calendar_items(self):
        return self._calendar_items

    def get_restaurants(self, tab):
        return json.loads(self._request('get', restaurants_url(tab)).content)['restaurantList']

    def list_dish(self, index=0):
        dishes = []
        tab = self.available_tabs()[index]
        restaurants = self.get_restaurants(tab)
        for restaurant in restaurants:
            restaurant_uid = restaurant['uniqueId']
            dishes.extend(
                json.loads(self._request('get', restaurant_dishes_url(tab, restaurant_uid)).content)['dishList'])
        return dishes

    def available_tabs(self):
        return reduce(lambda x, y: x + y, [filter(lambda x: x['status'] == 'AVAILABLE', _['calendarItemList'])
            for _ in self.calendar_items()['dateList']])

    def order(self, dish_id, index=0):
        tab = self.available_tabs()[index]
        return json.loads(self._request('post', order_url(tab, dish_id, address_uid)).content)

    def http_get(self, url, **kwargs):
        """
        :type url: str | unicode
        :rtype: dict | str | unicode
        """
        response = self._request('get', url, **kwargs)
        return json.loads(response.content)

    def http_post(self, url, data, **kwargs):
        """
        :type url: str | unicode
        :type data: dict
        :rtype: dict | str | unicode
        """
        response = self._request('post', url, data, **kwargs)
        return json.loads(response.content)

    def _request(self, method, url, data=None, **kwargs):
        """
        :type method: str | unicode
        :type url: str | unicode
        :type data: dict
        :type kwargs: dict
        :rtype: requests.Response
        """
        func = getattr(self._session, method)
        response = func(url, data=data, **kwargs)
        self.responses.append(response)
        return response
