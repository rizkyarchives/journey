from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class Analyzer():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.blacklisted_countries = ['Egypt', 'Turkey', 'Türkiye', 'Sri Lanka', 'Germany', 'Singapore']

    def analyze_link(self, links: list):
        full_data = []
        for link in links:
            self.driver.get(link)
            self.driver.maximize_window()
            try:
                cookie_button = self.driver.find_element(By.CSS_SELECTOR, '.ant-modal-body button')
                cookie_button.click()
                time.sleep(2)
            except NoSuchElementException:
                pass
            try:
                company_tag = self.driver.find_element(By.XPATH, '//*[@id="summary"]/div[1]/div/div[2]/div[2]').text
            except NoSuchElementException:
                company_tag = "Info Unavailable·Info Unavailable"
            company_country = company_tag.split('·')
            try:
                job_title = self.driver.find_element(By.XPATH, '//*[@id="summary"]/div[1]/div/div[2]/div[1]/h3').text
            except NoSuchElementException:
                job_title = "Info Unavailable"
            try:
                slots = self.driver.find_element(By.XPATH, '//*[@id="slots"]/div[2]').text.strip(' slots available to pick from')
            except NoSuchElementException:
                slots = "Info Unavailable"
            try:
                salary = self.driver.find_element(By.XPATH, '//*[@id="summary"]/div[2]/div[2]/h3').text
            except NoSuchElementException:
                salary = "Info Unavailable"
            try:
                intern_duration_tag = self.driver.find_element(By.XPATH, '//*[@id="slots"]/div[3]')
                opportunity_closes = intern_duration_tag.find_elements(By.CLASS_NAME, "text-grey-dark")[1].text.strip('Apply before ')
                intern_duration_as_list = intern_duration_tag.find_elements(By.CSS_SELECTOR, ".font-bold")
                intern_duration_as_list_of_string = [tag.text for tag in intern_duration_as_list]
                intern_duration = ", ".join(intern_duration_as_list_of_string)
            except NoSuchElementException:
                intern_duration = "Info Unavailable"
                opportunity_closes = "Info Unavailable"
            try:
                background = self.driver.find_element(By.XPATH, '//*[@id="summary"]/div[3]/div[2]/h3').text
            except NoSuchElementException:
                background = "Info Unavailable"
            try: 
                languages = self.driver.find_element(By.XPATH, '//*[@id="summary"]/div[4]/div[2]/h3').text
            except NoSuchElementException:
                languages = "Info Unavailable"
            try:
                country_preference_tag = self.driver.find_element(By.XPATH, '//*[@id="eligibility"]/div[5]/div[2]')
                country_preferences = country_preference_tag.find_elements(By.CSS_SELECTOR, '.ant-tag')
                country_preferences_list = [tag.text for tag in country_preferences]
                country_list_for_test = [country.strip('(Required)') for country in country_preferences_list]
                country_for_test = company_country[1].split(', ')
                countryPreference = ", ".join(country_list_for_test)
            except NoSuchElementException:
                countryPreference = "Info Unavailable"
            try:
                others_tag = self.driver.find_element(By.XPATH, '//*[@id="logistics"]/div/div[2]')
                others_tags = others_tag.find_elements(By.CLASS_NAME, 'ant-card-body')
                others_tag_list = [tag.text for tag in others_tags]
                others_final = others_tag_list[:-1]
                others = ", ".join(others_final)
            except NoSuchElementException:
                others = "Info Unavailable"
            languages_in_list = languages.split(', ')
            dont_submit = False
            if salary == "Unpaid":
                # print("Masuk unpaid")
                dont_submit = True
            if len(languages_in_list) > 2:
                # print("bahasa lebih dari 2")
                dont_submit = True
            if len(languages_in_list) == 2:
                if "Bahasa Indonesian" not in languages_in_list:
                    # print("bahasa lebih dari dua + gaada indo")
                    dont_submit = True
            if len(languages_in_list) == 1:
                if "Bahasa Indonesian" not in languages_in_list:
                    if "English" not in languages_in_list:
                        # print("Bahasa cuma 1 + gaada inggris ato indo")
                        dont_submit = True
            if 'Any Nationality' not in country_list_for_test:
                if 'Indonesia' not in country_list_for_test:
                    # print("Nationality bukan Any ato gaada Indo")
                    dont_submit = True
            try:
                if country_for_test[1] in self.blacklisted_countries:
                    # print("Blacklisted")
                    dont_submit = True
            except IndexError:
                if country_for_test[0] in self.blacklisted_countries:
                    # print("Blacklisted")
                    dont_submit = True
            if not dont_submit:
                data = {
                    'company': company_country[0],
                    'lcHost': '-',
                    'cityCountry': company_country[1],
                    'jobTitle': job_title,
                    'link': link,
                    'slots': slots,
                    'salary': salary,
                    'applicationCloses': opportunity_closes,
                    'internDuration': intern_duration,
                    'background': background,
                    'language': languages,
                    'countryPreference': countryPreference,
                    'others': others
                }
                # print(data)
                full_data.append(data)
            else:
                # print("gagal filter")
            time.sleep(1)
        return full_data
            


            

            

            
