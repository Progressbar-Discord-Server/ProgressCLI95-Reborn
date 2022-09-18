import sys
import time
import pcli_common as common
import utils


def check_modules() -> None:
    import subprocess
    import sys

    dependencies = []
    with open(utils.get_file_path('./dependencies.txt'),
              'r', encoding='utf8') as file:
        dependencies = file.readlines()

    print('Checking module dependencies...\n')

    installed = 0
    for module in dependencies:
        try:
            __import__(module)
        except ImportError:
            print(f'Module `{module}` not found, installing...')
            subprocess.run([sys.executable, '-m', 'pip', 'install', module, '--quiet'])
            installed += 1
        else:
            print(f'Module `{module}` found, dependency satisfied.')

    print(f'Dependencies satisfied, {installed} modules installed.\nStarting the game...')
    utils.clear_screen()


def main() -> None:
    from rich import print as rprint

    import settings
    import language
    settings.Settings()
    lang = language.Language()

    def print_bios_header():
        rprint(f'[white not bold]{lang.boot.sparrow_bios}[/white not bold] - [bright_yellow not bold]{lang.boot.energystar}[/bright_yellow not bold]')
        rprint(f'[white not bold]{lang.boot.version}[/white not bold]\n'.format(common.gamever, common.compile_date))
        if common.dev:
            rprint(f'\n[bold red]{lang.boot.dev_build}[/bold red]\n')

    print_bios_header()
    time.sleep(2)

    # It's very bad, but it's temporary
    while True:
        utils.clear_screen()
        print_bios_header()
        rprint(f'[bold]{lang.boot.enter_sys}[/bold]')
        rprint('[white not bold]1. Progressbar 95[/white not bold]')
        choice = input(f'{lang.boot.your_choice} > ')
        if choice != '1':
            rprint(f'[red]{lang.boot.choice_invalid}[/red]')
            input()
            continue
        import game.level
        lvl = game.level.GameLevel(number=1, system='95')
        lvl.play()


if __name__ == '__main__':
    check_modules()
    main()
