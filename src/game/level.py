from game.progressbar import Progressbar
from random import choices
from rich import print as rprint
import game.bsod
import game.segments
import time
import utils

class GameLevel:
    def __init__(self, *, number, system, type='Regular') -> None:
        self.bar = Progressbar()
        self.number = number
        self.system = system
        self.gamemode = type

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
        rprint(f'[italic]{self.gamemode}[/italic]')
        rprint(f'[bold]Level {self.number}[/bold]')

    def play(self) -> None:
        self.write_level_header()
        time.sleep(1)

        bsod = False
        while not self.bar.is_full() and not bsod:
            utils.clear_screen()
            self.write_level_header()

            rprint('[bold]Do you want to have this in your progressbar:[/bold]', end=' ')
            self.next_segment = self.get_next_segment()
            self.last_segments.append(self.next_segment)
            game.segments.draw_segment(self.next_segment)
            print('\n')

            print(f'Your progress bar: {int(self.bar.get_progress())}%')
            self.bar.draw()
            print()

            rprint('[bold]C[/bold] or [bold]Y[/bold] to catch, any other key to shy away:', end=' ')
            choice = input().lower().strip()
            if choice.startswith(('c', 'y')):
                bsod = self.bar.add_segment(self.next_segment)
        utils.clear_screen()
        if not bsod:
            rprint('[bold]You win![/bold]')
            print('Your bar:')
            self.bar.draw()
            return
        game.bsod.trigger()
