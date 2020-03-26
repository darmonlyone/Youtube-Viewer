import time

from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = "https://www.youtube.com/watch?v=on5E-FfLRGs"

driver: WebDriver = webdriver.Chrome("chromedriver.exe")

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
driver.get(url)
try:
    driver.find_element_by_class_name("ytp-large-play-button ").click()
    driver.find_element_by_class_name("ytp-mute-button").click()
except:
    pass
count = 1

while True:
    while True:
        if driver.current_url != url:
            print("finish:", count)
            break
    time.sleep(0.5)
    driver.get(url)
    time.sleep(1)
    count = count + 1
