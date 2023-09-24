from app.constants import COMMA_INDICATOR, RANGE_INDICATOR, STAR_INDICATOR, STEP_INDICATOR
from app.parsers import comma_parser, range_parser, step_parser, star_parser
from app.exception_handlers.validations import field_range_validation

class CronField:
    def __init__(self, cron_value, field_name):
        self.cron_value = cron_value
        self.field_name = field_name
        self.values = []

    def parse_field(self):
        '''Parse each field of cron string
        '''
        if self.cron_value.strip() == '':
            raise ValueError("Invalid Cron expression - Irregular spacing between the fields")
        if self.cron_value == STAR_INDICATOR:
            self.values = star_parser.parse(self.cron_value, self.field_name)

        elif COMMA_INDICATOR in self.cron_value:
            self.values = comma_parser.parse(self.cron_value, self.field_name)

        elif RANGE_INDICATOR in self.cron_value:
            self.values = range_parser.parse(self.cron_value, self.field_name)

        elif STEP_INDICATOR in self.cron_value:
            self.values = step_parser.parse(self.cron_value, self.field_name)
        else:
            field_range_validation(self.field_name, self.cron_value)
            self.values = [int(self.cron_value)]