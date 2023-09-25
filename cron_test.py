import unittest
from app.cron_string import CronString
from app.cron_field import CronField
from app.utils import tabulate_output

class TestCronParser(unittest.TestCase):
    def test_valid_cron_string(self):
        '''test cases for valid cron strings and their expected result
        '''
        valid_cron_strings = [
            ("*/15 0 1,15 * 1-5 /usr/bin/find", 
             """minute        0 15 30 45
hour          0
day of month  1 15
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr/bin/find"""),

            ("10-15 2/5 1,15,25 * 1-5 /usr", 
 """minute        10 11 12 13 14 15
hour          2 7 12 17 22
day of month  1 15 25
month         1 2 3 4 5 6 7 8 9 10 11 12
day of week   1 2 3 4 5
command       /usr""")
        ]
        for cron_string, expected_result in valid_cron_strings:
            cron_string = CronString(cron_string)
            result = cron_string.parse_string()
            result = tabulate_output(cron_string.fields, cron_string.cmd)
            self.assertEqual(result, expected_result)

    def test_invalid_cron_string(self):
        '''test cases for invalid cron strings and their exceptions as expected result
        '''
        invalid_cron_strings = [
            ("* * * *", ValueError),
            ("* * * * * * *", ValueError),
            ("60 * * * * *", ValueError), # Minute out of range - 60
            ("*/15 0 0,15 * 1-5 /usr/bin/find", ValueError), # Month out of range - 0
            ("*/15 1,2,3,4 1,15 10/15 -1-5 /usr", ValueError)
        ]
        
        for input_cron_string, expected_result in invalid_cron_strings:
            cron_string = CronString(input_cron_string)
            with self.assertRaises(expected_result):
                result = cron_string.parse_string()
                

    def test_valid_cron_field(self):
        '''test cases for valid cron strings and their expected result
        '''
        valid_cron_field_strings = [("10-15", "minute", [10, 11, 12, 13, 14, 15]),
                                    ("10/15", "minute", [10, 25, 40, 55]),
                                    ("19-23", "hour", [19, 20, 21, 22, 23]),
                                    ("23, 19", "hour", [23, 19]),
                                    ("7", "day of month", [7]),
                                    ("*/2", "month", [1,3,5,7,9,11]),
                                    ("1-6","day of week", [1,2,3,4,5,6]),
                                    ]
        for field_str, field_name, expected_result in valid_cron_field_strings:
            cron_field = CronField(field_str, field_name)
            cron_field.parse_field()
            assert cron_field.values == expected_result
    
    def test_invalid_cron_fields(self):
        '''test cases for invalid cron strings and their exceptions as expected result
        '''
        valid_cron_field_strings = [("55-60", "minute", ValueError), # out of range for minute (0-59)
                                    ("-1/15", "minute", ValueError), #-1/15 "-" considered range indicator
                                    ("24", "hour", ValueError), # out of range for hour (0-23)
                                    ("*/24", "hour", ValueError), # step value out of range
                                    ("31-10", "day of month", ValueError), # range min > range max
                                    ("0", "month", ValueError), # range for month(1-12)
                                    ("6,8","day of week", ValueError), # out of range for day of week (0-6)
                                    ]
        with self.assertRaises(ValueError):
            for field_str, field_name, expected_result in valid_cron_field_strings:
                cron_field = CronField(field_str, field_name)
                cron_field.parse_field()

if __name__ == '__main__':
    unittest.main()
