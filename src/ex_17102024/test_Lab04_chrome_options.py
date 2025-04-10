#Chrome Options

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import allure
import pytest

@allure.title("Chorme Options TC")
def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,600")
    # chrome_options.add_argument("--disable-infobars")   # doesn't support now
    chrome_options.add_argument("--headless")        # no UI, process running in the background


    driver = webdriver.Chrome(chrome_options)      # Creating the session
    driver.get("https://katalon-demo-cura.herokuapp.com/")     # Navigate to the URL
    #Chrome Incognito mode

    assert True == False

    # Stop the Python interpreter for 10 sec
    time.sleep(10)




