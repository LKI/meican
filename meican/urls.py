# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
import time

from utils import milli_to_datetime

one_week = datetime.timedelta(weeks=1)


def get_url(url):
    meican_url = 'https://meican.com/{}'
    return meican_url.format(url)


def login_url():
    return get_url('account/directlogin')


def meican_params(datas):
    d = {'noHttpGetCache': int(time.time() * 1000)}
    d.update(datas)
    p = '&'.join(['{}={}'.format(k, v) for (k, v) in d.items()])
    return p


def calender_items_url():
    today = datetime.datetime.today()
    begin_date = str(today.date())
    end_date = str((today + one_week).date())
    data = {
        'beginDate': begin_date,
        'endDate': end_date,
        'withOrderDetail': False,
    }
    return get_url('preorder/api/v2.1/calendarItems/list?{}'.format(meican_params(data)))


def restaurants_url(tab):
    uid = tab['userTab']['uniqueId']
    target_time = datetime.datetime.combine(
        milli_to_datetime(tab['targetTime']),
        datetime.time(hour=int(tab['openingTime']['closeTime'][:2]))
    )
    data = {
        'tabUniqueId': uid,
        'targetTime': target_time,
    }
    return get_url('preorder/api/v2.1/restaurants/list?{}'.format(meican_params(data)))


def order_url(tab, dish_id, address_uid):
    target_time = '{}+{}'.format(milli_to_datetime(tab['targetTime']), tab['openingTime']['closeTime'])
    order_string = '%5B%7B%22count%22:1,%22dishId%22:{}%7D%5D'.format(dish_id)
    data = {
        'corpAddressUniqueId': address_uid,
        'order': order_string,
        'tabUniqueId': tab['userTab']['uniqueId'],
        'targetTime': target_time,
        'userAddressUniqueId': address_uid,
    }
    return get_url('preorder/api/v2.1/orders/add?' + meican_params(data))


def restaurant_dishes_url(tab, restaurant_uid, ):
    target_time = '{}+{}'.format(milli_to_datetime(tab['targetTime']), tab['openingTime']['closeTime'])
    data = {
        'restaurantUniqueId': restaurant_uid,
        'tabUniqueId': tab['userTab']['uniqueId'],
        'targetTime': target_time,
    }
    return get_url('preorder/api/v2.1/restaurants/show?' + meican_params(data))
