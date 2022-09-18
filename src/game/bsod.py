def trigger(system: str='95') -> None:
    from rich import print as rprint
    import language

    lang = language.Language()

    # this is a mess
    # TODO: Universal message screen printer

    header = lang.bsod.bsod_header
    lines = [lang.bsod['bsod' + str(x)] for x in range(1, 5)]
    longest_len = max([len(x) for x in lines])
    window_width = longest_len + 2

    header_indent = (window_width - len(header)) // 2
    if header_indent * 2 + len(header) < window_width:
        window_width += 1
        header_indent += 1
        pass
    rprint('[white on #00007f]' + ' ' * window_width + '[/]')
    rprint('[bold white on #00007f]' + ' ' * header_indent + header + ' ' * header_indent + '[/]')
    rprint('[white on #00007f]' + ' ' * window_width + '[/]')
    rprint(f'[white on #00007f] {lang.bsod.bsod1}' + ' ' * (window_width - len(lang.bsod.bsod1) - 1) + '[/]')
    rprint(f'[white on #00007f] {lang.bsod.bsod2}' + ' ' * (window_width - len(lang.bsod.bsod2) - 1) + '[/]')
    rprint('[white on #00007f]' + ' ' * window_width + '[/]')
    rprint(f'[white on #00007f] {lang.bsod.bsod3}' + ' ' * (window_width - len(lang.bsod.bsod3) - 1) + '[/]')
    rprint(f'[white on #00007f] {lang.bsod.bsod4}' + ' ' * (window_width - len(lang.bsod.bsod4) - 1) + '[/]')
    rprint('[white on #00007f]' + ' ' * window_width + '[/]')
    input()
