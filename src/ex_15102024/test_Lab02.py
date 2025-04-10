# Selenium -> API representation details

from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome()
    # POST request to create a new FRESH copy of Chrome
    # Fresh - Chrome - Session ID - 6e31bb70-4809-4b20-8d87-cce289ef6e1


    driver.get("https://app.vwo.com")
    # Code -> HTTP Request - ChromeDriver(Selenium Manager) -> Chrome (Session ID)

    print(driver.title) # GET Request
    assert driver.title == "Login - VWO"