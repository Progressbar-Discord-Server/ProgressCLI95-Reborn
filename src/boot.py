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
            subprocess.run([sys.executable, '-m', 'pip',
                           'install', module, '--quiet'])
            installed += 1
        else:
            print(f'Module `{module}` found, dependency satisfied.')

    print(
        f'Dependencies satisfied, {installed} modules installed.\nStarting the game...')
    utils.clear_screen()


def main() -> None:
    from rich import print as rprint

    import game.level
    import language
    import save
    import settings
    settings.Settings()
    lang = language.Language()

    save_ = save.Save()

    rprint(
        f'[white not bold]{lang.boot.sparrow_bios}[/white not bold] - [bright_yellow not bold]{lang.boot.energystar}[/bright_yellow not bold]')
    rprint(f'[white not bold]{lang.boot.version}[/white not bold]\n'.format(
        common.gamever, common.compile_date))
    if common.dev:
        rprint(f'\n[bold red]{lang.boot.dev_build}[/bold red]\n')
    time.sleep(2)

    # temporary solution
    while True:
        lvl = game.level.GameLevel(number=int(
            save_.save_dict['systems']['pb95']['level']), system='95')
        if lvl.play():
            continue
        else:
            save_.save_dict['systems']['pb95']['level'] += 1
            rprint(
                f'[italic]Press Enter to continue or type "quit" to quit: [/italic]', end='')
            choice = input()
            if choice.lower().strip().startswith('quit'):
                break

    save_.write_save()


if __name__ == '__main__':
    check_modules()
    main()
