import json
import random
import sys

import utils


class Save:
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        path = utils.get_application_directory() / '1.pcli'
        self.save_dict = None
        if not path.exists():
            self.new_save()
        self.read_save()

    def new_save(self):
        path = utils.get_application_directory() / '1.pcli'
        path.touch(exist_ok=False)
        data = {
            'systems': {
                'pb95': {
                    'unlocked': True,
                    'level': 1,
                }
            }
        }
        self.write_save(data)

    def write_save(self, data=None):
        if data is None:
            data = self.save_dict
        path = utils.get_application_directory() / '1.pcli'
        with path.open('w') as file:
            json.dump(data, file, indent=4)

    def read_save(self):
        path = utils.get_application_directory() / '1.pcli'
        try:
            with path.open('r') as file:
                self.save_dict = json.load(file)
        except (json.JSONDecodeError, UnicodeDecodeError, OverflowError):
            self.corrupted_save_screen()

    def corrupted_save_screen(self):
        import language

        lang = language.Language()

        header = lang.save.corr_header
        lines: list[str] = []
        i = 1
        while True:
            key = 'corr' + str(i)
            if not key in lang.save:
                break
            lines.append(lang.save[key])
            i += 1
        utils.draw_message_screen(
            'white', '#00007f', [1, 1, 2, 1], header, *lines)
        input()
        utils.clear_screen()
        path = utils.get_application_directory() / '1.pcli'
        backup_name = utils.get_application_directory(
        ) / ('1-' + ('%030x' % random.randrange(16**30)) + '.pcli.bak')
        path.rename(backup_name)
        sys.exit(0)
