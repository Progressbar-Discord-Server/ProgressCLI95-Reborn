import binascii
import csv
import io
import random
import struct
import sys
import zlib

import pcli_common
import utils


class Save:
    _instance = None
    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        path = utils.get_application_directory() / '1.pcli'
        self.raw_save_data = b''
        self.save_dict = dict()
        if not path.exists():
            self.new_save()
        self.read_save()

    def new_save(self):
        path = utils.get_application_directory() / '1.pcli'
        path.touch(exist_ok=False)
        with path.open('wb') as file:
            sig = b'PCLI'
            gamever = pcli_common.gamever
            is_dev = pcli_common.dev
            fmt = pcli_common.save_file_format
            header = struct.pack(f'>4s4s?I', sig, gamever.encode('ascii'), is_dev, fmt)
            file.write(header)
            file.write(b'AE8aRVo/PDUgRQgZMVdeUQlxQSE=')

    def write_save(self):
        path = utils.get_application_directory() / '1.pcli'
        with path.open('wb') as file:
            sig = b'PCLI'
            gamever = pcli_common.gamever
            is_dev = pcli_common.dev
            fmt = pcli_common.save_file_format
            header = struct.pack(f'>4s4s?I', sig, gamever.encode('ascii'), is_dev, fmt)
            file.write(header)

            with io.StringIO() as csv_data:
                headers = list(self.save_dict[0].keys())
                writer = csv.DictWriter(csv_data, headers)
                writer.writeheader()
                writer.writerows(self.save_dict)
                encoded = utils.xor(csv_data.getvalue(), encode=True)
                file.write(encoded)

    def read_save(self):
        path = utils.get_application_directory() / '1.pcli'
        with path.open('rb') as file:
            sig = file.read(4)
            gamever = file.read(4).decode('ascii')
            _ = bool(file.read(1))  # unused
            fmt, = struct.unpack('>I', file.read(4))
            data = file.read().decode('ascii')

        try:
            self.raw_save_data = utils.xor(data, decode=True).decode('ascii')
        except (UnicodeDecodeError, binascii.Error):
            self.corrupted_save_screen()
        self.save_dict = list(csv.DictReader(self.raw_save_data.split('\n'), delimiter=','))
        print(self.save_dict)
        input()

        if not self.check_integrity(sig, gamever, fmt):
            self.corrupted_save_screen()

    def check_integrity(self, sig, gamever, fmt):
        if sig != b'PCLI':
            return False
        try:
            float(gamever)
        except ValueError:
            return False
        if fmt > pcli_common.save_file_format:
            return False

        for row in self.save_dict:
            data = ",".join(list(row.values())[:-1])
            hex_crc = f'{zlib.crc32(data.encode("ascii")):x}'.upper()
            if row['c'] != hex_crc:
                return False

        return True

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
        utils.draw_message_screen('white', '#00007f', [1, 1, 2, 1], header, *lines)
        input()
        utils.clear_screen()
        path = utils.get_application_directory() / '1.pcli'
        backup_name = utils.get_application_directory() / ('1-' + ('%030x' % random.randrange(16**30)) + '.pcli.bak')
        path.rename(backup_name)
        old_path = utils.get_application_directory() / '1.pcli'
        print(old_path)
        sys.exit(0)

    def get_value(self, parameter):
        for row in self.save_dict:
            if row['p'] == parameter:
                return row['v']

    def set_value(self, parameter, value):
        for row in range(len(self.save_dict)):
            if self.save_dict[row]['p'] == parameter:
                self.save_dict[row]['v'] = str(value)
                data = ",".join(list(self.save_dict[row].values())[:-1])
                hex_crc = f'{zlib.crc32(data.encode("ascii")):x}'.upper()
                self.save_dict[row]['c'] = hex_crc