def trigger(settings: dict, system: str='95') -> None:
    from rich import print as rprint
    rprint('[bold black on white]   GAME OVER   [/bold black on white]')
    print()
    print('A fatal mistake has been made by the player.')
    print('The current game session will be terminated')
    print()
    print('* Press Enter to terminate the current session')
    print("* Don't press CTRL+ALT+DEL to restart")
    input()