import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
    driver.quit()



