from app.constants import FIELD_DATA    

def validate_step_expression(cron_value, field_name):
    max_val = FIELD_DATA[field_name]["max"]
    min_val = FIELD_DATA[field_name]["min"]
    step_parts = cron_value.split('/')
    if len(step_parts) != 2:
        raise ValueError(f"Invalid cron field for {field_name}: {cron_value}")
    if step_parts[0] == "*":
        step_parts[0] = min_val
    else:
        try:
            step_parts[0] = int(step_parts[0])
        except:
            raise ValueError(f"Invalid cron field for {field_name}: {cron_value}- Expected integer or *")
    try:
        step_parts[1] = int(step_parts[1])
    except:
        raise ValueError(f"Invalid cron field for {field_name}: {cron_value}- Expected integer or *")
    
    if step_parts[0] < min_val or step_parts[1] > max_val:
        raise ValueError(f"Range out of bounds for {field_name}: {cron_value}")
    return step_parts


def validate_range_expression(cron_value, field_name):
    max_val = FIELD_DATA[field_name]["max"]
    min_val = FIELD_DATA[field_name]["min"]
    ranges = cron_value.split("-")
    if len(ranges) != 2:
        raise ValueError(f"Invalid cron field for {field_name}: {cron_value}")
    try:
        ranges[0] = int(ranges[0])
        ranges[1] = int(ranges[1])
    except:
        raise ValueError(f"Invalid cron field for {field_name}: {cron_value}- Expected integer")
    
    if ranges[0] < min_val or ranges[1] > max_val:
        raise ValueError(f"Range out of bounds for {field_name}: {cron_value}")
    return ranges
    

def field_range_validation(field_name, value):
    max_val = FIELD_DATA[field_name]["max"]
    min_val = FIELD_DATA[field_name]["min"]
    try:
        value = int(value)
    except:
        raise ValueError(f"Invalid Cron field for {field_name}: {value} -  Expected integer")
    if value < min_val or value > max_val:
           raise ValueError(f"Range out of bounds for {field_name}: {value}")
    return True