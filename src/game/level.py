from importlib import invalidate_caches
from random import choice
from rich import print as rprint
from game.progressbar import Progressbar
import game.segments
import utils

class GameLevel:
    def __init__(self, *, number, system, type='Regular') -> None:
        self.bar = Progressbar()
        self.number = number
        self.system = system
        self.type = type
        # TODO: Chances based on how high the level is
        self.segments_table = ('b', 'o', 'x2', 'x3', 'g', 'p', 'r', 'w')
        # TODO: They will affect the difficulty
        self.last_segments = []
        self.current_segment = ''

    def get_next_segment(self):
        return choice(self.segments_table)

    def play(self, settings: dict) -> None:
        invalid_choice = False
        while not self.bar.is_full():
            utils.clear_screen()

            rprint('[bold]Do you want to have this in your progressbar:[/bold]', end=' ')
            if not invalid_choice:
                self.current_segment = self.get_next_segment()
            game.segments.draw_segment(self.current_segment, settings)
            print('\n')
            print(f'Your bar: {int(self.bar.get_progress())}%')
            self.bar.draw(settings)
            print()
            rprint('[bold]\[C][/bold]atch | [bold]\[S][/bold]hy away:', end=' ')
            choice = input().lower().strip()

            if choice.startswith(('c', 'y')):
                self.bar.add_segment(self.current_segment)
                invalid_choice = False
            elif choice.startswith(('s', 'n')):
                invalid_choice = False
                continue
            else:
                invalid_choice = True
                continue
        utils.clear_screen()
        rprint('[bold]You win![/bold]')
        print('Your bar:')
        self.bar.draw(settings)
