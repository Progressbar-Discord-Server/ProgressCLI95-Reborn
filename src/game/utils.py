def load_settings() -> dict:
    import csv
    import utils

    settings = dict()
    with open(utils.get_file_path('./settings.pbcli')) as sf:
        settings_reader = csv.DictReader(sf)
        for row in settings_reader:
            settings[row['id']] = row['value']

    return settings
