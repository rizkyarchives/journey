from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

FILE_NAME = 'aiesec_links.txt'

# //*[@id="__next"]/div[2]/div[3]/div[2]/div[2]
class Compiler():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def compile_link(self, link: str):
        self.driver.get(link)
        cookie_button = self.driver.find_element(By.CSS_SELECTOR, '.ant-modal-body button')
        cookie_button.click()
        time.sleep(3)
        loading_more = True
        while loading_more:
            try:
                loadmore_button = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[3]/div[2]/div[3]/button[1]')
                the_text = loadmore_button.text
                if the_text == "Back to top":
                    loading_more = False
                ActionChains(self.driver).move_to_element(loadmore_button).click(loadmore_button).perform()
                time.sleep(3)
            except NoSuchElementException:
                loading_more = False
        div_link = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[3]/div[2]/div[2]')
        all_anchor_tag = div_link.find_elements(By.TAG_NAME, 'a')
        links = [tag.get_attribute("href") for tag in all_anchor_tag]
        self.driver.close()
        analyzed_links = self.read_opp_file()
        links_final = [link for link in links if link not in analyzed_links]
        with open(FILE_NAME, 'a') as file:
            for link in links_final:
                file.write((link) + "\n")
        return links_final
    
    def read_opp_file(self):
        with open(FILE_NAME, 'r') as file:
            opp_link_analyzed = file.readlines()
            opp_links = [string.strip() for string in opp_link_analyzed]
        
        return opp_links
            
