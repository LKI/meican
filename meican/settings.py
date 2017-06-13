# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from os.path import exists, expanduser, join

from meican.utils import json_dump, prompt

setting_file = join(expanduser('~'), '.meicanrc')


class MeiCanSetting(object):
    def __init__(self):
        self._settings = {}
        if not exists(setting_file):
            return
        with open(setting_file) as f:
            self._settings = json.load(f)

    def save(self):
        with open(setting_file, b'w') as f:
            f.write(json_dump(self._settings))

    def load_credentials(self):
        for key in ['username', 'password']:
            if key not in self._settings:
                self._settings[key] = prompt('please input your meican {}: '.format(key))
        self.save()

    def __getattr__(self, item):
        return self._settings[item]
