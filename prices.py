# https://selenium-python.readthedocs.io
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ebay_sold_items_url = 'https://www.ebay.co.uk/'

def get_driver():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

#to run for this script only
if __name__ == "__main__":
    print('Creatiing driver')
    driver = get_driver()

    print('fetching the page')
    driver.get(ebay_sold_items_url)
    print('Page title', driver.title)

    #click advanced filter
    advanced_link = driver.find_element(By.LINK_TEXT, "Advanced")
    advanced_link.click()

    # explicit wait
    try:
        time.sleep(5)
        sold_filter = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="gdpr-banner-accept"]')
        ))
        sold_filter.click()

       
    except:
        driver.quit()
    
    print('searching for item')
    
    #click sold items filter
    time.sleep(5)
    sold_link = driver.find_element(By.ID, "LH_Sold")
    sold_link.click()

    searh_bar_id = '_nkw'
    search_bar = driver.find_element(By.ID, searh_bar_id)
    # make sure search bar is empty
    search_bar.clear()
    search_bar.send_keys("ps5")
    #press enter
    search_bar.send_keys(Keys.RETURN)

    #get the listed items
    listed_items_class = 'sresult lvresult clearfix li' 
    listed_items  = driver.find_element(By.CLASS_NAME, listed_items_class)
    print(f'Found {len(listed_items)} items.')
    # driver.quit()




