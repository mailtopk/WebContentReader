
import get_visa_dates as gvd
import helperutil as hutil

print('******** Bot Started *********************')

try :

    # Create class instance
    visa_bulletion = gvd.CheckVisaBulletion()
    visa_bulletion.init_webdriver()

    comparing_months_url = visa_bulletion.get_current_and_next_month_links()

    if len(comparing_months_url) == 1:
        hutil.print_pretty_title('Visa bulletion yet to release.')
    else: 
        # Array of data frames
        emp_visa_bulletion_info = []

        for comparing_month_url_count in range(0, len(comparing_months_url)):
            print("Reading dates for " + comparing_months_url[comparing_month_url_count])
            df = visa_bulletion.read_employment_final_dates(comparing_months_url[comparing_month_url_count])
            trimmed_dataframe = df.query("Employment_based in ['1st','2nd', '3rd']")[['Employment_based', 'INDIA', 'CHINA_mainland born']]
            emp_visa_bulletion_info.append(trimmed_dataframe)

        # Compare 
        if (emp_visa_bulletion_info[0].eq(emp_visa_bulletion_info[1])).all().all():
            print('\nNo change in dates for India and China')
       
        hutil.print_pretty_title('India Employment Dates')

         # India Eb1
        print('\nIndia EB 1')
        eb1_india_value_current_month = hutil.format_date(emp_visa_bulletion_info[0].at[1, 'INDIA'])
        eb1_india_value_next_month =  hutil.format_date(emp_visa_bulletion_info[1].at[1, 'INDIA'])
        print("Current Month :" + eb1_india_value_current_month + "\n" + "Next Month :" + eb1_india_value_next_month)
        
        print('\nIndia EB 2')
        eb2_india_value_current_month = hutil.format_date(emp_visa_bulletion_info[0].at[2, 'INDIA'])
        eb2_india_value_next_month = hutil.format_date(emp_visa_bulletion_info[1].at[2, 'INDIA'])
        print("Current Month :" + eb2_india_value_current_month + "\n" + "Next Month :" + eb2_india_value_next_month)

        print('\nIndia EB 3')
        eb3_india_value_current_month = hutil.format_date(emp_visa_bulletion_info[0].at[3, 'INDIA'])
        eb23_india_value_current_month = hutil.format_date(emp_visa_bulletion_info[1].at[3, 'INDIA'])
        print("Current Month :" + eb3_india_value_current_month + "\n" + "Next Month :" + eb23_india_value_current_month)


        hutil.print_boarder_line()

        for i in range(0, len(emp_visa_bulletion_info)):
            print(emp_visa_bulletion_info[i])
            #print(emp_visa_bulletion_info[i].query("Employment_based in ['1st','2nd', '3rd']")[['Employment_based', 'INDIA', 'CHINA_mainland born']])

finally:
    visa_bulletion.cleanup()



print('******** End of bot *********************')