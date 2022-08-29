import csv
import utils

class Settings:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        with open(utils.get_file_path('./settings.pbcli'), 'r', encoding='utf8') as file:
            self.settings = dict()
            settings_reader = csv.DictReader(file)
            for row in settings_reader:
                self.settings[row['id']] = {
                    'type': row['type'],
                    'default': row['default'],
                    'value': row['value'],
                }

    def get_value(self, setting: str):
        return self.settings[setting]['value']

    def get_converted_value(self, setting: str):
        type = self.get_type(setting)
        val = self.get_value(setting)
        if type == 'int':
            return int(val)
        elif type == 'str' or type == 'choice':
            return val
        elif type == 'bool':
            return val == 'True'

    def get_type(self, setting: str):
        return self.settings[setting]['type']

    def get_default(self, setting: str):
        return self.settings[setting]['default']
