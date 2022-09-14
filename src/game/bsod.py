def trigger(system: str='95') -> None:
    from rich import print as rprint
    rprint('[bold #00007f on white]   GAME OVER   [/bold #00007f on white][white on #00007f]                               [/]')
    rprint('[white on #00007f]                                              [/]')
    rprint('[white on #00007f]A fatal mistake has been made by the player.  [/]')
    rprint('[white on #00007f]The current game session will be terminated   [/]')
    rprint('[white on #00007f]                                              [/]')
    rprint('[white on #00007f]* Press Enter to terminate the current session[/]')
    rprint("[white on #00007f]* Don't press CTRL+ALT+DEL to restart         [/]")
    rprint('[white on #00007f]                                              [/]')
    input()
