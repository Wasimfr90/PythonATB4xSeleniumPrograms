from selenium import webdriver
import pytest
import allure


def test_open_vwo_login():
    driver = webdriver.Chrome()     # Create the session
    driver.get("https://app.vwo.com") # Navigate to URL
    page_source_data = driver.page_source
    print(page_source_data)


