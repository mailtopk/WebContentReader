import pandas as pd
import sys
import helperutil as util
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckVisaBulletion :
    
    page_source = ''
    __url = ''
    customOptions = Options()
    config = util.get_config()
    

    def __init__(self) :
        self.customOptions.add_argument('--headless')
        self.customOptions.add_argument('-disable-gpu')
        self.__url = self.config['visabulletin']['mainpage'] 
        

    def init_webdriver(self):
        self.driver = webdriver.Chrome( options = self.customOptions)
        
    def cleanup(cls):
        if cls.driver != None and cls.driver.service.process :
            cls.driver.quit()
            cls.driver = None

    #def is_visa_release_date_within_window():


    # build the dates string
    def get_current_and_next_month_links(cls):
        cls.driver.get(cls.__url)

        cls.page_source = cls.driver.page_source
        current_month_num = str(datetime.now().month)
        strip_current_month = datetime.strptime(current_month_num, "%m")
        current_month = 'visa-bulletin-for-' + strip_current_month.strftime("%B") + '-' + str(datetime.now().year) + '.html'

        next_month_num = str(datetime.now().month +1)
        strip_next_month_num =  datetime.strptime(next_month_num, "%m")
        next_month = 'visa-bulletin-for-' + strip_next_month_num.strftime("%B") + '-' + str(datetime.now().year) + '.html'

        return (cls.__get_visa_date_href_of_month([current_month, next_month]), strip_next_month_num.strftime("%B") + '-' + str(datetime.now().year))
    
    
    def __get_visa_date_href_of_month(self, months):
        months_url = []

        for i in range(0, len(months)):
            xpath = "//a[contains(@href,'" + months[i].lower() + "')]"
            try:
                links = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, xpath)))

                for lnk in links:
                    href = lnk.get_attribute('href')
                    if href is not None:
                        if not href in months_url: # ignore duplicate.
                            months_url.append(href)
            except TimeoutException as e:
                return months_url
            except Exception as ex: 
                print(f"An error occured in : {sys._getframe().f_code.co_name} Error : {str(ex)}")
                self.cleanup()
            
        return months_url
    
    # opn the url and read table
    def read_employment_final_dates(self, url_link):
        if url_link is None :
            print("Invalid url")
            return
        try:
            self.driver.get(url_link)
            results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//table/tbody')))
            df_table = pd.DataFrame()
            table_rows = []

            #for tbody in results:
            if len(results) > 0:
                tbody= results[7] # for now read only employment
                tr = tbody.find_elements(By.TAG_NAME, 'tr')
                
                for tr_count in range(0, len(tr)) :
                    td = tr[tr_count].find_elements(By.TAG_NAME,  'td')
                    table_rows.clear()
                    for td_count in range(0, len(td)):
                        if tr_count == 0 :
                            col_name = td[td_count].text.replace('\n',"")
                            col_name = col_name.replace('-','_') # '-' is not supported by df
                            df_table[col_name] = 0 # Poulate datafram header
                            continue
                        table_rows.append(td[td_count].text.replace('\n',"")) 
                    
                    if len(table_rows) != 0:
                        df_table.loc[tr_count] = table_rows # Populate dataframe rows
            return df_table
        except Exception as e : 
            print(e)




 
