from app.constants import (
    STAR_INDICATOR, 
    STEP_INDICATOR, 
    RANGE_INDICATOR,
    COMMA_INDICATOR
    )
from app.parsers import step_parser, range_parser
from app.exception_handlers.validations import field_range_validation

def parse(cron_value, field_name):
    values = []
    partitions = cron_value.split(COMMA_INDICATOR)
    for part in partitions:
        if part == STAR_INDICATOR:
            continue
        if STEP_INDICATOR in part:
            values.extend(step_parser.parse(cron_value, field_name))

        elif RANGE_INDICATOR in part:
            values.extend(range_parser.parse(cron_value, field_name))
        else:
            field_range_validation(field_name, part)
            values.append(int(part))
    return values