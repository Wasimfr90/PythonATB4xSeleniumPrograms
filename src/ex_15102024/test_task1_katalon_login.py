#Task 1
# Try the Selenium IDE, Record the One Test
# open this → https://katalon-demo-cura.herokuapp.com/
# Click on the button Make appointment
# on the Next Page → Enter the username, password and submit button
# Export the script to Python.


from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

def test_katalon_login_page():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # button = driver.find_element("Make Appointment")
    button = driver.find_element(By.ID, "btn-make-appointment")
    button.click()

    print(driver.title)
    assert driver.title == "CURA Healthcare Service"