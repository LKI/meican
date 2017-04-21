# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import Tab


def get_tabs_from_calendar_items(data):
    """
    :type data: dict
    :rtype: list[meican.models.Tab]
    """
    date_list = data['dateList']
    tabs = []
    for day in date_list:
        tabs.extend([Tab(_) for _ in day['calendarItemList']])
    return tabs
