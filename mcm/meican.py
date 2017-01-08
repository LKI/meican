# coding=utf-8 #
from __future__ import unicode_literals

import json

import requests

from urls import login_url, calender_items_url, restaurants_url, get_url, meican_params
from utils import milli_to_datetime

favorite = "af5431"

address_uid = "e7b93aafd597"


class Session:
    def __init__(self, username, password):
        self._session = requests.Session()
        self.responses = []
        self.login(username, password)

    def login(self, username, password):
        form_data = {"username": username, "password": password, "loginType": "username", "remember": True}
        response = self.query("post", login_url(), form_data)
        if 200 != response.status_code:  # or "用户名或密码错误" in response.content:
            raise Exception("login fail because username or password incorrect")
        return response

    def query(self, method, url, data=None):
        return self.save_response(getattr(self._session, method)(url, data=data))

    def save_response(self, response):
        self.responses.append(response)
        return response

    def calendar_items(self):
        if not hasattr(self, "_calendar"):
            self._calendar = json.loads(self._session.get(calender_items_url()).content)
        return self._calendar

    def get_restaurants(self, tab):
        return json.loads(self._session.get(restaurants_url(tab)).content)

    def list_dish(self, index=0):
        tab = self.available_tabs()[index]
        target_time = "{}+{}".format(milli_to_datetime(tab['targetTime']), tab['openingTime']['closeTime'])
        data = {
            "restaurantUniqueId": favorite,
            "tabUniqueId": tab['userTab']['uniqueId'],
            "targetTime": target_time,
        }
        return json.loads(self.query(
            "get", get_url("preorder/api/v2.1/restaurants/show?" + meican_params(data))).content)['dishList']

    def available_tabs(self):
        return reduce(lambda x, y: x + y, [filter(lambda x: x['status'] == 'AVAILABLE', _['calendarItemList'])
                                           for _ in self.calendar_items()['dateList']])

    def order(self, dish_id, index=0):
        tab = self.available_tabs()[index]
        target_time = "{}+{}".format(milli_to_datetime(tab['targetTime']), tab['openingTime']['closeTime'])
        order_string = "%5B%7B%22count%22:1,%22dishId%22:{}%7D%5D".format(dish_id)
        data = {
            "corpAddressUniqueId": address_uid,
            "order": order_string,
            "tabUniqueId": tab['userTab']['uniqueId'],
            "targetTime": target_time,
            "userAddressUniqueId": address_uid,
        }
        return self.query("post", get_url("preorder/api/v2.1/orders/add?" + meican_params(data))).content
