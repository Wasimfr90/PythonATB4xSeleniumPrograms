#Chrome Options - Parallel run

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import allure
import pytest

@allure.title("Chorme Options TC")
def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

def test_edge_current_url_verification():
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()
    # driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

# def test_firefox_current_url_verification():
#     # driver = webdriver.Chrome()
#     # driver = webdriver.Edge()
#     driver = webdriver.Firefox()
#     driver.get("https://katalon-demo-cura.herokuapp.com/")
#     assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
#     time.sleep(10)
#     driver.quit()





