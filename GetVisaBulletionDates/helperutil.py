import datetime
import yaml
import os

def print_pretty_title(message):
    print('*'.center(60, '*'))
    print('\t' + message)
    print('*'.center(60, '*'))

def print_boarder_line():
    print("#".center(60, '#'))

# print date as 1st of January.
def format_date(date_str):
    input_format = "%d%b%y"
    date = datetime.datetime.strptime(date_str, input_format)
    day = date.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    output_format = "{day}{suffix} of {month} {year}"
    return output_format.format(day=day, suffix=suffix, month=date.strftime("%B"), year=date.year)

def get_config():
    current_file_path = os.path.realpath(__file__)
    current_dir = os.path.dirname(current_file_path)
    config_file_path = os.path.join(current_dir, 'config.yaml')
    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file)
        return config





