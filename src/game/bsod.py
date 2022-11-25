def trigger(system: str='95') -> None:
    import language
    import utils

    lang = language.Language()

    header = lang.bsod.bsod_header
    lines: list[str] = []
    i = 1
    while True:
        key = 'bsod' + str(i)
        if not key in lang.bsod:
            break
        lines.append(lang.bsod[key])
        i += 1
    utils.draw_message_screen('white', '#00007f', [1, 1, 2, 1],
                              header, *lines)
    input()
