# coding=utf-8 #
import json
import requests

from urls import login_url, calender_items_url


class Session:
    def __init__(self, username, password):
        self.session = requests.Session()
        self.responses = []
        self.login(username, password)

    def login(self, username, password):
        form_data = {"username": username, "password": password, "loginType": "username", "remember": True}
        self.query("post", login_url(), form_data)

    def query(self, method, url, data):
        self.save_response(getattr(self.session, method)(url, data=data))

    def save_response(self, response):
        self.responses.append(response)

    def calendar_items(self):
        return json.loads(self.session.get(calender_items_url()).content)


class Formatter:
    def __init__(self):
        pass

    @classmethod
    def json_data(self, data):
        return json.dumps(data, ensure_ascii=False, indent=2).encode("utf8")
