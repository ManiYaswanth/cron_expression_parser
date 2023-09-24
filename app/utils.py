def get_range_values(ranges):
    start = ranges[0]
    end = ranges[1]
    return list(range(start, end + 1))


def get_step_values(step_values, min_val, max_val):
    values = []
    start = step_values[0]
    step = step_values[1]
    # for value in range(start, max_val + 1):
    #     if (value - min_val) % step == 0:
    #         values.append(value)
    values = list(range(start, max_val + 1))[::step]
    return values

def tabulate_output(cron_fields, cron_command):
    output_table = []
    for cron_field in cron_fields:
        output_table.append(f"{cron_field.field_name:<14}{' '.join(map(str, cron_field.values))}")

    output_table.append(f"{'command':<14}{cron_command}")

    return "\n".join(output_table)