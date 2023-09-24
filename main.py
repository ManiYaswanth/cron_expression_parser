from app.cron_string import CronString
from app.utils import tabulate_output
from sys import argv

def main():
    input_string = argv[1]
    cron_string = CronString(input_string)
    cron_string.parse_string()
    output = tabulate_output(cron_string.fields, cron_string.cmd)
    print(output)


if __name__ == '__main__':
    main()