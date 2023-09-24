COMMA_INDICATOR = ','
RANGE_INDICATOR = '-'
STAR_INDICATOR = '*'
STEP_INDICATOR = '/'
FIELD_NAMES = ["minute", "hour", "day of month", "month", "day of week"]

FIELD_DATA = {"minute": {"name": "minute", "max": 59, "min": 0},
               "hour" :{"name": "hour", "max": 23, "min": 0}, 
               "day of month": {"name": "day of month", "max": 31, "min": 1}, 
               "month": {"name": "month", "max": 12, "min": 1}, 
               "day of week": {"name": "day of week", "max": 6, "min": 0}
            }