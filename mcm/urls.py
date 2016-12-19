# coding=utf-8 #

import datetime
import time

one_week = datetime.timedelta(weeks=1)


def get_url(url):
    meican_url = "https://meican.com/{}"
    return meican_url.format(url)


def login_url():
    return get_url("account/directlogin")


def meican_params(datas):
    d = {"noHttpGetCache": int(time.time() * 1000)}
    d.update(datas)
    p = "&".join(["{}={}".format(k, v) for (k, v) in d.items()])
    return p


def calender_items_url():
    today = datetime.datetime.today()
    begin_date = str(today.date())
    end_date = str((today + one_week).date())
    data = {
        "beginDate": begin_date,
        "endDate": end_date,
        "withOrderDetail": False,
    }
    return get_url("preorder/api/v2.1/calendarItems/list?{}".format(meican_params(data)))


def restaurants_url(tab):
    uid = tab['userTab']['uniqueId']
    target_time = (datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=tab["targetTime"])) \
        .replace(hour=int(tab["openingTime"]["closeTime"][:2]))
    data = {
        "tabUniqueId": uid,
        "targetTime": target_time,
    }
    return get_url("preorder/api/v2.1/restaurants/list?{}".format(meican_params(data)))
