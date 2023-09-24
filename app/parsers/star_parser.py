from app.constants import FIELD_DATA

def parse(cron_value, field_name):
    parsed_values = list(range(FIELD_DATA[field_name]["min"], FIELD_DATA[field_name]["max"] + 1))
    return parsed_values