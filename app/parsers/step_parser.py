from app.constants import FIELD_DATA
from app.utils import get_step_values
from app.exception_handlers.validations import validate_step_expression

def parse(cron_value, field_name):
    '''
    Validate cron_value, splitting by / and getting valid values
    '''
    step_parts = validate_step_expression(cron_value, field_name)
    values = get_step_values(step_parts, FIELD_DATA[field_name]["min"], FIELD_DATA[field_name]["max"])
    return values