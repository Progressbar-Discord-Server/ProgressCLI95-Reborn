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


def check_settings():
    import os
    import utils
    if os.path.exists(utils.get_file_path('./settings.pbcli')):
        return
    with open(utils.get_file_path('./settings.pbcli'), 'w', encoding='utf8') as file:
        import csv

        writer = csv.writer(file)
        writer.writerows([
            ['id', 'type', 'default', 'value'],
            ['ascii_mode','bool','False','False'],
            ['colorblind','bool','False','False']
        ])


def main() -> None:
    import game.level
    import game.utils

    settings = game.utils.load_settings()

    lvl = game.level.GameLevel(number=1, system='95')
    lvl.play(settings)


if __name__ == '__main__':
    check_modules()
    check_settings()
    main()
