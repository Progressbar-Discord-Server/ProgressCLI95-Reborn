import time
from random import choices

from rich import print as rprint

import game.bsod
import game.segments
import language
import utils
from game.progressbar import Progressbar

lang = language.Language()

class GameLevel:
    def __init__(self, *, number, system, gamemode='regular') -> None:
        self.bar = Progressbar()
        self.number = number
        self.system = system
        self.gamemode = gamemode

        self.next_segment = ''
        self.segment_weights = self.generate_segment_weights()
        # TODO: Chances based on how high the level is
        self.segments_table = ('b', 'o', 'x2', 'x3', 'g', 'p', 'r', 'w')
        # TODO: They will affect the difficulty
        self.last_segments = []

    def generate_segment_weights(self) -> None:
        # Weights are relative
        initial_weights = [
            200,  # blue
            200,  # orange
            75,   # light blue (x2)
            70,   # light blue (x3)
            110,  # gray
            120,  # pink
            145,  # red
            5,    # green
        ]

        # TODO: Tweak weights based on many factors

        return initial_weights

    def get_next_segment(self) -> str:
        return choices(self.segments_table, weights=self.segment_weights, k=1)[0]

    def write_level_header(self):
        rprint(f'[italic]{lang.gamemode[self.gamemode]}[/italic]')
        rprint(f'[white bold]{lang.game.level_n}[/white bold]'.format(self.number))

    def play(self) -> None:
        utils.clear_screen()
        self.write_level_header()
        time.sleep(1)

        bsod = False
        while not self.bar.is_full() and not bsod:
            utils.clear_screen()
            self.write_level_header()

            rprint(f'[bold]{lang.game.do_you_want_to_have}[/bold]', end=' ')
            self.next_segment = self.get_next_segment()
            game.segments.draw_segment(self.next_segment)
            print('\n')

            print(f'{lang.game.your_bar} {int(self.bar.get_progress())}%')
            self.bar.draw()
            print()

            rprint(f'{lang.game.press_to_catch}', end=' ')
            choice = input().lower().strip()
            if choice.startswith(('c', 'y')):
                bsod = self.bar.add_segment(self.next_segment)
        utils.clear_screen()
        if not bsod:
            rprint(f'[bold]{lang.game.win}[/bold]')
            print(f'{lang.game.your_bar}')
            self.bar.draw()
            return False
        game.bsod.trigger()
        return True
