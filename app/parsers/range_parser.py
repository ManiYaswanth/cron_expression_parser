from app.constants import FIELD_DATA
from app.utils import get_range_values
from app.exception_handlers.validations import validate_range_expression

def parse(cron_value, field_name):
    ranges = validate_range_expression(cron_value, field_name)
    values = get_range_values(ranges)
    return values