import datetime
import yaml
import os

def print_pretty_title(message):
    print('\n')
    print('*'.center(60, '*'))
    print('\t' + message)
    print('*'.center(60, '*'))

def print_boarder_line():
    print('\n')
    print("#".center(60, '#'))

def print_boarder_line_with_center(message):
    print('\n')
    print(message.center(60, '#'))

# formate date from 
def format_date(date):
    # Split the date into day, month, and year
    day = date[:2]
    month = date[2:5]
    year = date[5:]

    if month == "JAN": month = "January"
    elif month == "FEB": month = "February"
    elif month == "MAR": month = "March"
    elif month == "APR": month = "April"
    elif month == "MAY": month = "May"
    elif month == "JUN": month = "June"
    elif month == "JUL": month = "July"
    elif month == "AUG": month = "August"
    elif month == "SEP": month = "September"
    elif month == "OCT": month = "October"
    elif month == "NOV": month = "November"
    elif month == "DEC": month = "December"

    # Add the ordinal suffix to the day
    if day[-1] == '1':
        day += 'st'
    elif day[-1] == '2':
        day += 'nd'
    elif day[-1] == '3':
        day += 'rd'
    else:
        day += 'th'

    # Return the formatted date
    return f'{month} {day}, {year}'


# Read config file
def get_config():
    current_file_path = os.path.realpath(__file__)
    current_dir = os.path.dirname(current_file_path)
    config_file_path = os.path.join(current_dir, 'config.yaml')
    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file)
        return config


# DF frame structure
#   Employment_based    INDIA             CHINA_mainland born
# 1              1st  01FEB22             01FEB22
# 2              2nd  08OCT11             08JUN19
# 3              3rd  15JUN12             01AUG18

# Compare two dates 01FEB22 to 1st of February 2022
def compare_dates(date1, date2):
    date1 = datetime.datetime.strptime(date1, '%d%b%y') # expected formate is 01FEB22
    date2 = datetime.datetime.strptime(date2, '%d%b%y')
    delta = date1 - date2
    return delta.days

def compare_and_print_india_eb1_details(emp_visa_bulletion_info):
    country = 'INDIA'
    eb1_date1 = emp_visa_bulletion_info[0].at[1, country] #1st row 2nd column 
    eb1_date2 = emp_visa_bulletion_info[1].at[1, country]

    delta = compare_dates(eb1_date1, eb1_date2)

    priority_date = f"Current month priority date is: {format_date(eb1_date1)} Next month priority date is: {format_date(eb1_date2)}"
    short_statement = "\nIndia EB 1 - "
    if delta < 0 :
        print(f"{short_statement} BACKWARD MOMENT")
        print(f"There is a BACKWARD MOMENT for Eb1 {country} by {delta}. {priority_date}")
    elif delta == 0 :
        print(f"{short_statement} NO MOMENT")
        print(f"There is NO MOMENT for Eb1 {country}. {priority_date} ")
    else :
        print(f"{short_statement} FORWARD MOMENT")
        print(f"Good News!! There is FORWARD MOMENT for Eb1 by {delta} days. {priority_date}")


def compare_and_print_india_eb2_details(emp_visa_bulletion_info):
    country = 'INDIA'

    eb2_date1 = emp_visa_bulletion_info[0].at[2, country] #2rd row 2nd column 
    eb2_date2 = emp_visa_bulletion_info[1].at[2, country]

    delta = compare_dates(eb2_date1, eb2_date2)
    priority_dates = f"Current month priority date is: {format_date(eb2_date1)} Next month priority date is {format_date(eb2_date2)}"
    short_statement = "\nIndia EB 2 - "

    if delta < 0 :
        print(f"{short_statement} BACKWORD MOMENT")
        print(f"There is a BACKWARD MOMENT for Eb2 {country} by {delta} . {priority_dates}")
    elif delta == 0 :
        print(f"{short_statement} NO MOMENT" )
        print(f"There is NO MOMENT for Eb2 {country}. {priority_dates}")
    else :
        print(f"{short_statement} FORWARD MOMENT")
        print(f"Good News!! There is FORWARD MOMENT for Eb2 by {delta} days. {priority_dates}")


def compare_and_print_india_eb3_details(emp_visa_bulletion_info):
    country = 'INDIA'
    eb3_date1 = emp_visa_bulletion_info[0].at[3, country] #3rd row 2nd column 
    eb3_date2 = emp_visa_bulletion_info[1].at[3, country]

    delta = compare_dates(eb3_date1, eb3_date2)
    short_statement = "\nIndia EB 3 - "
    priority_dates = f"Current month priority date is: {format_date(eb3_date1)} Next month priority date is: {format_date(eb3_date2)}"  
    if delta < 0 :
        print(f"{short_statement} BACKWORD MOMENT")
        print(f"There is a BACKWARD MOMENT for Eb3 {country} by {delta}. {priority_dates}")
    elif delta == 0 :
        print(f"{short_statement} NO MOMENT")
        print(f"There is NO MOMENT for Eb3 {country}. {priority_dates} ")
    else :
        print(f"{short_statement} FORWARD MOMENT")
        print(f"Good News!! There is FORWARD MOMENT for Eb3 by {delta} days. {priority_dates}")


#China Eb1
def compare_and_print_china_eb1_details(emp_visa_bulletion_info):
    country = 'CHINA_mainland born'
    eb1_date1 = emp_visa_bulletion_info[0].at[1, country] #1st row 3nd column 
    eb1_date2 = emp_visa_bulletion_info[1].at[1, country]

    delta = compare_dates(eb1_date1, eb1_date2)
    short_statement = "\nChina EB 1 - "
    priority_dates = f"Current month priority date is: {format_date(eb1_date1)} Next month priority date is: {format_date(eb1_date2)}"
    if delta < 0 :
        print(f"{short_statement} BACKWORD MOMENT")
        print(f"There is a BACWORD MOMENT for Eb1 CHINA by {delta}. {priority_dates}")
    elif delta == 0 :
        print(f"{short_statement} NO MOMENT")
        print(f"There is NO MOMENT for Eb3 CHINA. {priority_dates} ")
    else :
        print(f"{short_statement} FORWARD MOMENT")
        print(f"Good News!! There is FORWARD MOMENT for Eb3 by CHINA days. {priority_dates} ")

 #China Eb2
def compare_and_print_china_eb2_details(emp_visa_bulletion_info):
    country = 'CHINA_mainland born'
    eb2_date1 = emp_visa_bulletion_info[0].at[2, country] #1st row 3nd column 
    eb2_date2 = emp_visa_bulletion_info[1].at[2, country]

    delta = compare_dates(eb2_date1, eb2_date2)
    priority_dates =  f"Current month priority date is: {format_date(eb2_date1)} Next month priority is: {format_date(eb2_date2)}"
    short_statement = "\nChina EB 2 - "
    if delta < 0 :
        print(f"{short_statement} BACKWARD MOMENT")
        print(f"There is a BACKWARD MOMENT for Eb2 CHINA by {delta}. {priority_dates}")
    elif delta == 0 :
        print(f"{short_statement} No MOMENT")
        print(f"There is NO MOMENT for Eb2 CHINA. {priority_dates}. {priority_dates} ")
    else :
        print(f"{short_statement} FORWARD MOMENT")
        print(f"Good News!!. There is a FORWARD MOMENT for Eb2 by CHINA days. {priority_dates}")
        
        #China Eb3
def compare_and_print_china_eb3_details(emp_visa_bulletion_info):
    country = 'CHINA_mainland born'
    eb3_date1 = emp_visa_bulletion_info[0].at[1, country] #1st row 3nd column 
    eb3_date2 = emp_visa_bulletion_info[1].at[1, country]

    delta = compare_dates(eb3_date1, eb3_date2)
    priority_dates = f"Current month priority date is: {format_date(eb3_date1)}. Next month priorityis:  {format_date(eb3_date2)}"
    short_statement = "\nChina EB 3 - "
    if delta < 0 :
        print(f"{short_statement} BACKWARD MOMENT")
        print(f"There is a BACKWARD MOMENT for Eb3 CHINA by {delta}. {priority_dates}")
    elif delta == 0 :
        print(f"{short_statement} NO MOMENT")
        print(f"There is NO MOMENT for Eb3 CHINA. {priority_dates} ")
    else :
        print(f"{short_statement} FORWARD MOMENT")
        print(f"Good News!! There is a FORWARD MOMENT for Eb3 by CHINA days. {priority_dates}")
