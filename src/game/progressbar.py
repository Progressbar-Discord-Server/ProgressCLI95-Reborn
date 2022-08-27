import typing
from rich import print as rprint
import game.segments

class Progressbar:
    def __init__(self, *, segments: typing.Union[str, tuple, list]='', width: int=20) -> None:
        self.segments = list(segments)
        self.width = width

    def get_progress(self):
        return len(self.segments) / self.width * 100

    def is_empty(self):
        return len(self.segments) == 0

    def is_full(self):
        return len(self.segments) >= self.width

    def add_segment(self, segment: str):
        if segment == 'b':
            self.segments.append('b')
        elif segment == 'x2':
            self.segments.append('b')
            self.segments.append('b')
        elif segment == 'x3':  # :P
            self.segments.append('b')
            self.segments.append('b')
            self.segments.append('b')
        elif segment == 'o':
            self.segments.append('o')
        elif segment == 'g':
            return
        elif segment == 'p' and not self.is_empty():
            self.remove_last_segments()
        elif segment == 'r':
            print('you lose') # todo
            exit()  # XD
        elif segment == 'w':
            self.segments = list('b' * self.width)
        else:
            print('whar')

    def remove_last_segments(self, amount: int=1):
        for i in range(amount):
            self.segments.pop()

    def draw(self, settings: dict) -> None:
        bar_top, bar_bottom, bar_side, seg_width = '', '', '', 0
        if (settings['ascii_mode'] == 'True'):
            seg_width = 2
            bar_top = bar_bottom = f'+{"-" * self.width * 2}+'
            bar_side = '|'
        else:
            seg_width = 1
            bar_middle = '━' * self.width
            bar_top = f'┏{bar_middle}┓'
            bar_bottom = f'┗{bar_middle}┛'
            bar_side = '┃'

        rprint(bar_top)
        rprint(bar_side, end='')

        drawn_segments = self.segments.copy()
        if len(drawn_segments) < self.width:
            for i in range(self.width - len(drawn_segments)):
                drawn_segments.append(' ')
        while len(drawn_segments) > self.width:
            drawn_segments.pop()
        for segment in drawn_segments:
            if segment == ' ':
                rprint(' ' * seg_width, end='')
                continue
            game.segments.draw_segment(segment, settings, in_bar=True)
        rprint(bar_side)
        rprint(bar_bottom)
