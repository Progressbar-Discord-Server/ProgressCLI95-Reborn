def trigger(system: str='95') -> None:
    from rich import print as rprint
    import language

    lang = language.Language()

    rprint(f'[white on #00007f]                 [/white on #00007f][bold #00007f on white]   {lang.bsod.bsod_header}   [/bold #00007f on white][white on #00007f]                 [/white on #00007f]')
    rprint(f'[white on #00007f]                                                 [/white on #00007f]')
    rprint(f'[white on #00007f] {lang.bsod.bsod1}    [/white on #00007f]')
    rprint(f'[white on #00007f] {lang.bsod.bsod2}     [/white on #00007f]')
    rprint(f'[white on #00007f]                                                 [/white on #00007f]')
    rprint(f'[white on #00007f] {lang.bsod.bsod3}  [/white on #00007f]')
    rprint(f"[white on #00007f] {lang.bsod.bsod4}           [/white on #00007f]")
    rprint(f'[white on #00007f]                                                 [/white on #00007f]')
    input()
