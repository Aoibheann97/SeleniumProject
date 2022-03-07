from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import commands
import random, string

try:

    # # Path for Chrome driver
    driver = webdriver.Chrome("/Users/admin/chromedriver")

    #Open Teachable
    driver.get("https://takehome.zeachable.com")

    #Random Email
    randomEmail = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(15)) + "@test.com"

    #Click Login
    commands.loginButton(driver)

    #Click Sign Up
    driver.find_element(by=By.XPATH, value= '/html/body/main/div/form/div[5]/a').click()

    #No Entry
    commands.signupUser("", "", "", driver, False ,False)

    driver.back()

    #Invalid Entry
    commands.signupUser("", "test", "", driver, False, False)

    driver.back()

    #Valid Entry
    commands.signupUser("Teachable Test", "test@test.com", "password", driver, True, True)

    driver.back()

    #Valid Entry
    commands.signupUser("Teachable Test", randomEmail, "password", driver, True, True)

    driver.close()

except Exception as err:
   print('Selenium script failed : ', err.__class__, "occurred.")
