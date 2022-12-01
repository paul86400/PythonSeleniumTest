from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    # Some browsers may have an info bar that displays info such as memory is low. Those popup bars may interfere with the script so we disable them.
    options.add_argument("disable-infobars")
    # Some web pages may change the content when you re-size the browser so it's better to maximize it right away.
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")


    driver = webdriver.Chrome(options=options)
    driver.get("http://testphp.vulnweb.com/login.php")
    time.sleep(2)

    # locate username, password, and submit elements
    username = driver.find_element(By.XPATH, "//input[@name='uname']")
    password = driver.find_element(By.XPATH, "//input[@name='pass']")
    submit   = driver.find_element(By.XPATH, "//input[@type='submit']")

    # input username and password and click login
    username.send_keys("test")
    time.sleep(1)
    password.send_keys("test")
    time.sleep(1)

    submit.click()
    time.sleep(2)

    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div/div[2]/div[1]/p")
    return element.text

print (main())
