from multiprocessing.sharedctypes import Value
import time
from rich import print as rprint
import csv
import os
import utils

class Settings:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not os.path.exists(utils.get_file_path('./settings.pbcli')):
            Settings.create_settings()
        Settings.fetch_settings()

    @classmethod
    def fetch_settings(cls):
        with open(utils.get_file_path('./settings.pbcli'), 'r', encoding='utf8') as file:
            cls._instance.settings = dict()
            settings_reader = csv.DictReader(file)
            for row in settings_reader:
                cls._instance.settings[row['id']] = {
                    'type': row['type'],
                    'default': row['default'],
                    'value': row['value'],
                }

    def create_settings(autofetch=True):
        with open(utils.get_file_path('./settings.pbcli'), 'w', encoding='utf8') as file:
            writer = csv.writer(file)
            writer.writerows([
                ['id',         'type', 'default', 'value'],
                ['ascii_mode', 'bool', 'False',   'False'],
                ['colorblind', 'bool', 'False',   'False']
            ])
        if autofetch:
            Settings.fetch_settings()

    def fix_settings():
        utils.clear_screen()
        rprint('[bold black on white]   Uh-oh!   [/bold black on white]')
        print('Seems like your settings file is corrupted!')
        print()
        print('Press Enter to regenerate your settings file and quit the game.')
        input()
        Settings.create_settings()
        exit(0)

    def safe_get(self, setting: str, key: str):
        result = None
        try:
            result = self.settings[setting][key]
        except KeyError:
            Settings.fix_settings()
        return result

    def get_value(self, setting: str):
        return self.safe_get(setting, 'value')

    def get_type(self, setting: str):
        return self.safe_get(setting, 'type')

    def get_default(self, setting: str):
        return self.safe_get(setting, 'default')

    def get_converted_value(self, setting: str):
        type = self.get_type(setting)
        val = self.get_value(setting)
        try:
            if type == 'int':
                return int(val)
            elif type == 'str' or type == 'choice':
                return val
            elif type == 'bool':
                if not (val in ('True', 'False')):
                    raise ValueError
                return val == 'True'
            else:
                Settings.fix_settings()
        except (TypeError, ValueError):
            Settings.fix_settings()
