import utils


def check_modules():
    import os.path
    import subprocess
    import sys

    dependencies = []
    with open(os.path.join(os.path.dirname(__file__), './dependencies.txt'),
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


def main():
    pass


if __name__ == '__main__':
    check_modules()
    main()
