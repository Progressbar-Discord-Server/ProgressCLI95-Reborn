import os
import pathlib
import sys


class SemVer:
    def __init__(self, stage: str, major: int, minor: int, patch: int):
        self.stage = stage
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self) -> str:
        return f'{self.stage}-{self.major}.{self.minor}.{self.patch}'

    def __repr__(self):
        return str(self)


class DotDict(dict):
    def __getattr__(*args):
        val = dict.get(*args)
        if type(val) is dict:
            val = DotDict(val)
        return val
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def clear_screen() -> None:
    if sys.platform.startswith(('win32')):
        os.system('cls')
    elif sys.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        os.system('clear')


def get_appdata_directory() -> pathlib.Path:
    home = pathlib.Path.home()

    if sys.platform.startswith(('win32')):
        return home / 'AppData' / 'Local'
    if sys.platform.startswith(('linux')):
        return home / '.local' / 'share'
    if sys.platform.startswith(('darwin')):
        return home / 'Library' / 'Application Support'
    return None


def get_application_directory() -> pathlib.Path:
    appdata_dir = get_appdata_directory()
    if appdata_dir is None:
        return None
    app_dir = appdata_dir / 'ProgressCLI95'
    if app_dir.exists():
        pass
    else:
        app_dir.mkdir(parents=True)
    return app_dir


def get_game_root() -> pathlib.Path:
    return pathlib.Path('.')


# it works.
def get_file_path(filename: str) -> str:
    """Get file path relative to utils.py"""
    import os.path

    return os.path.join(os.path.dirname(__file__), filename)


def draw_message_screen(foreground: str, background: str, indent: list, header: str, *lines):
    from rich import print as rprint

    longest_line = max([len(line) for line in lines])
    window_width = longest_line + indent[0] + indent[2]
    header_indent_width = (window_width - len(header)) // 2
    if header_indent_width * 2 + len(header) < window_width:
        window_width += 1
        header_indent_width += 1

    header_indent = ' ' * header_indent_width

    empty_line = f'[on {background}]' + ' ' * window_width + '[/]'

    for _ in range(indent[1]):
        rprint(empty_line)

    rprint(f'[bold {foreground} on {background}]' +
           header_indent + header + header_indent + '[/]')
    rprint(empty_line)

    for line in lines:
        left_indent = ' ' * indent[0]
        right_indent = ' ' * (window_width - len(line) - 1)
        rprint(f'[{foreground} on {background}]' +
               left_indent + line + right_indent + '[/]')

    for _ in range(indent[3]):
        rprint(empty_line)
