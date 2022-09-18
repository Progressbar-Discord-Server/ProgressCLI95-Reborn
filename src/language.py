import utils

class Language:
    _instance = None
    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self._lang_obj = None

    def set_lang(self, lang: str):
        import json

        filename = utils.get_file_path(f'lang/{lang}.json')
        with open(filename, 'r', encoding='utf8') as file:
            self._lang_obj = utils.DotDict(json.load(file))

    def __getattr__(self, *args):
        if not self._lang_obj:
            self.set_lang('en_US')
        return self._lang_obj.__getattr__(*args)
