# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta, timezone
from enum import Enum

import six


class TabStatus(Enum):
    AVAIL = 'AVAILABLE'
    CLOSED = 'CLOSED'
    NOT_YET = 'NOT_YET'
    UNKNOWN = 'UNKNOWN'
    ORDERED = 'ORDERED'

    @classmethod
    def parse(cls, string_value):
        """
        :type string_value: str | unicode
        :rtype: TabStatus
        """
        value_enums = {
            'AVAILABLE': cls.AVAIL,
            'CLOSED': cls.CLOSED,
            'NOT_YET': cls.NOT_YET,
            'ORDER': cls.ORDERED,
        }
        return value_enums.get(string_value, cls.UNKNOWN)


class ReadableObject(object):
    def __repr__(self):
        return six.text_type(self)


class Address(ReadableObject):
    """ 地址 """

    def __init__(self, data):
        """
        :type data: dict
        """
        self.uid = data['uniqueId']
        self.address = data['address']  # 公司地址
        self.pick_up = data['pickUpLocation']  # 取餐地址

    def __repr__(self):
        return '{} {}'.format(self.uid, self.address)


class Tab(ReadableObject):
    """
    一个 Tab 代表一个时间窗口
    比如 中饭点餐时间
    或者 晚饭点餐时间
    """

    def __init__(self, data):
        """
        :type data: dict
        """
        self.title = data['title']
        self.target_time = datetime.fromtimestamp(int(data['targetTime']) / 1000, tz=timezone(timedelta(hours=8)))
        self.status = TabStatus.parse(data['status'])
        self.uid = data['userTab']['uniqueId']
        self.addresses = [Address(_) for _ in data['userTab']['corp']['addressList']]

    def __repr__(self):
        return '{} {} {}'.format(self.status.value, self.target_time.strftime('%Y-%m-%d'), self.title)


class Restaurant(ReadableObject):
    """ 餐厅 """

    def __init__(self, tab, data):
        """
        :type tab: Tab
        :type data: dict
        """
        self.tab = tab
        self.uid = data['uniqueId']
        self.name = data['name']
        self.is_open = data['open']
        self.rating = data['rating']
        self.tel = data['tel']
        self.latitude = data['latitude']
        self.longitude = data['longitude']

    def __repr__(self):
        return '{}'.format(self.name)


class Dish(ReadableObject):
    """ 菜 """

    def __init__(self, restaurant, data):
        """
        :type restaurant: Restaurant
        :type data: dict
        """
        self.restaurant = restaurant
        self.id = int(data['id'])
        self.name = data['name']
        self.price = data['priceString']

    def __repr__(self):
        return '{}'.format(self.name)
