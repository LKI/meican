# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from functools import reduce

import requests

from meican.exceptions import MeiCanError
from urls import calender_items_url, login_url, order_url, restaurant_dishes_url, restaurants_url

address_uid = 'e7b93aafd597'  # 再惠


class RestUrl(object):
    """ 用来存储 MeiCan Rest 接口的类 """

    @classmethod
    def get_base_url(cls, path):
        return 'https://meican.com/{}'.format(path)

    @classmethod
    def login(cls):
        return cls.get_base_url('account/directlogin')


class MeiCan(object):
    def __init__(self, username, password):
        """
        :type username: str | unicode
        :type password: str | unicode
        """
        self._session = requests.Session()
        self.responses = []
        self.login(username, password)
        self._calendar = json.loads(self._session.get(calender_items_url()).content)

    def http_post(self, url, data, **kwargs):
        """
        :type url: str | unicode
        :type data: dict
        :rtype: dict | str | unicode
        """
        response = self._request('', url, data, **kwargs)
        return json.loads(response.content)

    def login(self, username, password):
        form_data = {'username': username, 'password': password, 'loginType': 'username', 'remember': True}
        response = self._request('post', login_url(), form_data)
        if 200 != response.status_code:  # or '用户名或密码错误' in response.content:
            raise MeiCanError('login fail because username or password incorrect')
        return response

    def save_response(self, response):
        self.responses.append(response)
        return response

    def calendar_items(self):
        return self._calendar

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
