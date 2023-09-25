from app.constants import FIELD_DATA    

def validate_step_expression(cron_value, field_name):
    '''
    args: cron_value with step indicator, field_name
    splits by / and validates each part
    return: validated and parsed step_parts
    '''
    max_val = FIELD_DATA[field_name]["max"]
    min_val = FIELD_DATA[field_name]["min"]
    step_parts = cron_value.split('/')
    if len(step_parts) != 2:
        raise ValueError(f"Invalid cron field for {field_name}: {cron_value}")
    if step_parts[0] == "*":
        step_parts[0] = min_val
    for idx, val in enumerate(step_parts):
        step_parts[idx] = field_range_validation(field_name, val)
    return step_parts


def validate_range_expression(cron_value, field_name):
    '''
    args: cron_value of the field and field name
    splits by range and validates
    return: valid parsed range
    '''
    ranges = cron_value.split("-")
    if len(ranges) != 2:
        raise ValueError(f"Invalid cron field for {field_name}: {cron_value}")
    for idx, val in enumerate(ranges):
        ranges[idx] = field_range_validation(field_name, val)
    
    return ranges
    

def field_range_validation(field_name, value):
    '''
    args: field_name and part of cron_value
    Checks if the value falls in range of cron field
    return: parsed value
    '''
    max_val = FIELD_DATA[field_name]["max"]
    min_val = FIELD_DATA[field_name]["min"]
    try:
        value = int(value)
    except:
        raise ValueError(f"Invalid Cron field for {field_name}: {value} -  Expected integer")
    if value < min_val or value > max_val:
           raise ValueError(f"Range out of bounds for {field_name}: {value}")
    return value
