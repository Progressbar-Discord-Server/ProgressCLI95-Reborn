from rich import print as rprint
import csv
import language
import os
import utils


lang = language.Language()

class Settings:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not os.path.exists(utils.get_file_path('./settings.pbcli')):
            self.create_settings()
        self.fetch_settings()

    def fetch_settings(self):
        with open(utils.get_file_path('./settings.pbcli'), 'r', encoding='utf8') as file:
            self.settings = dict()
            settings_reader = csv.DictReader(file)
            for row in settings_reader:
                self.settings[row['id']] = {
                    'type': row['type'],
                    'default': row['default'],
                    'value': row['value'],
                }

    def create_settings(self, autofetch=True):
        with open(utils.get_file_path('./settings.pbcli'), 'w', encoding='utf8') as file:
            writer = csv.writer(file)
            writer.writerows([
                ['id',         'type', 'default', 'value'],
                ['ascii_mode', 'bool', 'False',   'False'],
                ['colorblind', 'bool', 'False',   'False'],
            ])
        if autofetch:
            self.fetch_settings()

    def fix_settings(self):
        utils.clear_screen()
        rprint(f'[bold black on white]   {lang.settings.uhoh}   [/bold black on white]')
        print(lang.settings.corr1)
        print()
        print(lang.settings.corr_regen)
        input()
        self.create_settings()
        exit(0)

    def safe_get(self, setting: str, key: str):
        result = None
        try:
            result = self.settings[setting][key]
        except KeyError:
            self.fix_settings()
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
                self.fix_settings()
        except (TypeError, ValueError):
            self.fix_settings()
