
import get_visa_dates as gvd
import helperutil as hutil

def main():
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
            #if (emp_visa_bulletion_info[0].eq(emp_visa_bulletion_info[1])).all().all():
            #    print('\nNo change in dates for India and China')
        
            hutil.print_pretty_title('India Employment Dates')

            # India Eb1
            hutil.compare_and_print_india_eb1_details(emp_visa_bulletion_info)
            
            # India Eb2
            hutil.compare_and_print_india_eb2_details(emp_visa_bulletion_info)

            # India EB3
            hutil.compare_and_print_india_eb3_details(emp_visa_bulletion_info)

            hutil.print_pretty_title('China Employment Dates')
            
            #China Eb1
            hutil.compare_and_print_china_eb1_details(emp_visa_bulletion_info)

            #China Eb2
            hutil.compare_and_print_china_eb2_details(emp_visa_bulletion_info)

            #China Eb3
            hutil.compare_and_print_china_eb3_details(emp_visa_bulletion_info)


            hutil.print_boarder_line()

            for i in range(0, len(emp_visa_bulletion_info)):
                print(f"\n{emp_visa_bulletion_info[i]}")
                #print(emp_visa_bulletion_info[i].query("Employment_based in ['1st','2nd', '3rd']")[['Employment_based', 'INDIA', 'CHINA_mainland born']])

    finally:
        visa_bulletion.cleanup()

if __name__ == "__main__":
    hutil.print_boarder_line_with_center(' Start ')
    main()
    hutil.print_boarder_line_with_center (' End of bot ')


