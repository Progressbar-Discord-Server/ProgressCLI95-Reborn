import typing
from rich import print as rprint
import game.segments

class Progressbar:
    def __init__(self, *, segments: typing.Union[str, tuple, list]='', width: int=20) -> None:
        self.segments = list(segments)
        self.width = width

    def get_progress(self) -> float:
        return len(self.segments) / self.width * 100

    def is_empty(self) -> bool:
        return len(self.segments) == 0

    def is_full(self) -> bool:
        return len(self.segments) >= self.width

    def add_segment(self, segment: str) -> bool:
        if segment == 'b':
            self.segments.append('b')
        elif segment == 'x2':
            for _ in range(2):
                self.add_segment('b')
        elif segment == 'x3':
            for _ in range(3):
                self.add_segment('b')
        elif segment == 'o':
            self.segments.append('o')
        elif segment == 'g':
            return False
        elif segment == 'p' and not self.is_empty():
            self.remove_last_segment()
        elif segment == 'r':
            return True
        elif segment == 'w':
            self.segments = list('b' * self.width)
        else:
            print('whar')
        return False

    def remove_last_segment(self) -> str:
        return self.segments.pop()

    def draw(self, settings: dict) -> None:
        seg_width = game.segments.get_segment_width(settings)
        bar_top, bar_bottom, bar_side = '', '', ''
        if (settings['ascii_mode'] == 'True'):
            bar_top = bar_bottom = f'+{"-" * self.width * 2}+'
            bar_side = '|'
        else:
            bar_middle = '━' * self.width
            bar_top = f'┏{bar_middle}┓'
            bar_bottom = f'┗{bar_middle}┛'
            bar_side = '┃'

        rprint(bar_top)
        rprint(bar_side, end='')

        drawn_segments = self.segments.copy()
        if len(drawn_segments) < self.width:
            for _ in range(self.width - len(drawn_segments)):
                drawn_segments.append(' ')
        while len(drawn_segments) > self.width:
            drawn_segments.pop()
        for segment in drawn_segments:
            if segment == ' ':
                rprint(' ' * seg_width, end='')
                continue
            game.segments.draw_segment(settings, segment, in_bar=True)
        rprint(bar_side)
        rprint(bar_bottom)
