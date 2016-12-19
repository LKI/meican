# coding=utf-8 #
import json

import requests

from urls import login_url, calender_items_url, restaurants_url


class Session:
    def __init__(self, username, password):
        self._session = requests.Session()
        self.responses = []
        self.login(username, password)

    def login(self, username, password):
        form_data = {"username": username, "password": password, "loginType": "username", "remember": True}
        self.query("post", login_url(), form_data)

    def query(self, method, url, data):
        self.save_response(getattr(self._session, method)(url, data=data))

    def save_response(self, response):
        self.responses.append(response)

    def calendar_items(self):
        if not hasattr(self, "_calendar"):
            self._calendar = json.loads(self._session.get(calender_items_url()).content)
        return self._calendar

    def get_restaurants(self, tab):
        return json.loads(self._session.get(restaurants_url(tab)).content)

    def order(self):
        # get available restaurants
        available_order_tabs = reduce(
            lambda x, y: x + y,
            [filter(lambda x: x['status'] == 'AVAILABLE',
                    _['calendarItemList']) for _ in self.calendar_items()['dateList']])
        restaurants = map(lambda x: self.get_restaurants(x), available_order_tabs)
        # todo get restaurant dishes
        # todo order dishes
        return restaurants


class Formatter:
    def __init__(self):
        pass

    @classmethod
    def json_data(self, data):
        return json.dumps(data, ensure_ascii=False, indent=2).encode("utf8")
