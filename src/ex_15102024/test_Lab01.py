from selenium import webdriver
import pytest
import allure

@allure.title("Verify the title of the webpage app.vwo.com")
def test_sample():

    # Selenium 3 - Not much use now
    # driver_path = "/user/wasim/Downloads/edge/msedgedriver"
    # driver = webdriver.edgeServices(executable_path= driver_path)
    # driver.get("https://app.vwo.com")

    # Selenium 4 (Selenium Manager) - who will download the driver by itself
    # driver = webdriver.Chrome()
    # driver.get("https://sdet.live")

    driver = webdriver.Edge()
    driver.get("https://google.com")
    assert driver.current_url == "https://www.google.com"


