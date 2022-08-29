from rich import print as rprint

def draw_segment(settings: dict, segment: str, system: str='95', *, in_bar: bool=False) -> int:
    def colored(contents: str):
        return f'[{get_segment_color(segment)}]{contents}[/{get_segment_color(segment)}]'

    seg = ''
    if settings['ascii_mode'] == 'True':
        if not in_bar and settings['colorblind'] == 'True':
            seg += colored('\[')
            seg += get_segment_char(segment)
            seg += colored(']')
        else:
            seg += colored('\[]')
    else:
        if not in_bar and settings['colorblind'] == 'True':
            seg += f'[on {get_segment_color(segment)}]{get_segment_char(segment)}[/on {get_segment_color(segment)}]'
        else:
            seg += colored('█')

    if segment in ('x2', 'x3') and not in_bar:
        seg += ' ' + segment

    rprint(seg, end='')


def get_segment_width(settings: dict, *, in_bar: bool=False):
    if settings['ascii_mode'] == 'True':
        if not in_bar and settings['colorblind'] == 'True':
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
        return ' '
    elif segment == 'o':
        return ' '
    elif segment == 'x2' or segment == 'x3':
        return ' '
    elif segment == 'g':
        return '0'
    elif segment == 'p':
        return '-'
    elif segment == 'r':
        return '!'
    elif segment == 'w':
        return 'v'
    else:
        return '?'  # :)
