import json
from os.path import exists, expanduser, join

setting_file = join(expanduser("~"), ".meicanrc")


class MeiCanSetting(object):
    def __init__(self):
        self._settings = {}
        if not exists(setting_file):
            return
        with open(setting_file, encoding="utf-8") as f:
            self._settings = json.load(f)

    def save(self):
        with open(setting_file, str("w"), encoding="utf-8") as f:
            f.write(json.dumps(self._settings, ensure_ascii=False, indent=2))

    def load_credentials(self):
        for key in ["username", "password"]:
            if key not in self._settings:
                self._settings[key] = input("please input your meican {}: ".format(key))
        self.save()

    def __getattr__(self, item):
        return self._settings[item]
