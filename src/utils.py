class DotDict(dict):
    def __getattr__(*args):
        val = dict.get(*args)
        if type(val) is dict:
            val = DotDict(val)
        return val
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def clear_screen() -> None:
    import os
    import sys

    if sys.platform.startswith(('win32')):
        os.system('cls')
    elif sys.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        os.system('clear')


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

    rprint(f'[bold {foreground} on {background}]' + header_indent + header + header_indent + '[/]')
    rprint(empty_line)

    for line in lines:
        left_indent = ' ' * indent[0]
        right_indent = ' ' * (window_width - len(line) - 1)
        rprint(f'[{foreground} on {background}]' + left_indent + line + right_indent + '[/]')

    for _ in range(indent[3]):
        rprint(empty_line)
