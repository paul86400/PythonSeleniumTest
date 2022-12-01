from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# open firefox
browser = webdriver.Firefox()

# navigate to website and wait
browser.get("http://testphp.vulnweb.com/login.php")
time.sleep(2)

# locate username, password, and submit elements
username = browser.find_element(By.XPATH, "//input[@name='uname']")
password = browser.find_element(By.XPATH, "//input[@name='pass']")
submit   = browser.find_element(By.XPATH, "//input[@type='submit']")

# input username and password and click login
username.send_keys("test")
time.sleep(1)
password.send_keys("test")
time.sleep(1)

submit.click()

print("Test complete.")

browser.close()