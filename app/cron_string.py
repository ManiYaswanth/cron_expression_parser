from app.constants import FIELD_NAMES
from app.cron_field import CronField

class CronString:
    def __init__(self, cron_string: str):
        self.cron_string = cron_string
        self.fields = []
        self.cmd = None

    def parse_string(self):
        ''' split the cron string by space
          map the fields, create CronField object
          parse each field'''
        fields = self.cron_string.split()
        if len(fields) != 6:
            raise ValueError("Invalid Cron expression")
        fields = self.cron_string.split(' ', 5)
        self.cmd = fields[-1]
        if len(fields[-1].strip()) != len(self.cmd):
            raise ValueError("Invalid Cron expression - Irregular spacing between the fields")
        for i, field in enumerate(fields[:-1]):
            field_name = FIELD_NAMES[i]
            cron_field  = CronField(field, field_name)
            cron_field.parse_field()
            self.fields.append(cron_field)
        return self
