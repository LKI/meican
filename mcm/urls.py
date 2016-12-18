# coding=utf-8 #

import datetime
import time

one_week = datetime.timedelta(weeks=1)


def get_url(url):
    meican_url = "https://meican.com/{}"
    return meican_url.format(url)


def login_url():
    return get_url("account/directlogin")


def calender_items_url():
    today = datetime.datetime.today()
    begin_date = str(today.date())
    end_date = str((today + one_week).date())
    milli_second = int(time.time() * 1000)
    data = {
        "beginDate": begin_date,
        "endDate": end_date,
        "noHttpGetCache": milli_second,
        "withOrderDetail": False,
    }
    params = "&".join(["{}={}".format(k, v) for (k, v) in data.items()])
    return get_url("preorder/api/v2.1/calendarItems/list?{}".format(params))
