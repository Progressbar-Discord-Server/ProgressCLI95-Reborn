from rich import print as rprint
from settings import Settings

def draw_segment(segment: str, system: str='95', in_bar: bool=False) -> int:
    def colored(contents: str):
        return f'[{get_segment_color(segment)}]{contents}[/{get_segment_color(segment)}]'

    seg = ''
    if Settings().get_converted_value('ascii_mode'):
        if not in_bar and Settings().get_converted_value('colorblind'):
            seg += colored('\[')
            seg += get_segment_char(segment)
            seg += colored(']')
        else:
            seg += colored('\[]')
    else:
        if not in_bar and Settings().get_converted_value('colorblind'):
            seg += f'[on {get_segment_color(segment)}]{get_segment_char(segment)}[/on {get_segment_color(segment)}]'
        else:
            seg += colored('█')

    if segment in ('x2', 'x3') and not in_bar:
        seg += ' ' + segment

    rprint(seg, end='')


def get_segment_width(in_bar: bool=False):
    if Settings().get_converted_value('ascii_mode'):
        if not in_bar and Settings().get_converted_value('colorblind'):
            return 3
        else:
            return 2
    else:
        return 1


# temporary
def get_segment_color(segment: str, system: str='95') -> str:
    if segment == 'b':
        return '#00007f'
    elif segment == 'o':
        return '#f7931e'
    elif segment == 'x2' or segment == 'x3':
        return '#29abe2'
    elif segment == 'g':
        return '#9e9e9e'
    elif segment == 'p':
        return '#ff00ff'
    elif segment == 'r':
        return '#c1272d'
    elif segment == 'w':
        return '#8cc63f'
    else:
        return '#ed1e79'  # :)


def get_segment_char(segment: str, system: str = '95') -> str:
    if segment == 'b':
        return '[bold #f7931e]B[/]'
    elif segment == 'o':
        return '[bold #00007f]Y[/]'
    elif segment == 'x2' or segment == 'x3':
        return '[bold white]B[/]'
    elif segment == 'g':
        return '[black]0[/]'
    elif segment == 'p':
        return '[bold #9e9e9e]-[/]'
    elif segment == 'r':
        return '[bold #9e9e9e]![/]'
    elif segment == 'w':
        return '[bold #c1272d]√[/]'
    else:
        return '[bold white]?[/]'  # :)
