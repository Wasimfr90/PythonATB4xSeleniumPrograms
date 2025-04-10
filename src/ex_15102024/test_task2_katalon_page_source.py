# Task 2:
# Create a Selenium Script to verify the title for
# Open the Page - https://katalon-demo-cura.herokuapp.com/
# Verify the current URL, current title
# In the page source add a assertion that “CURA Healthcare Service” exist in the page. driver.pageSource() - String


from selenium import webdriver
import pytest
import allure

def test_katalon_login_page():
    driver = webdriver.Chrome()               # Creating the session
    driver.get("https://katalon-demo-cura.herokuapp.com/")     # navigate to the URL

    print(driver.title)
    assert driver.title == "CURA Healthcare Service"

    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    #print(page_source_data)

    driver.quit()