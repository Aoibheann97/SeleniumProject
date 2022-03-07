from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import commands

try:
    # # Path for Chrome driver
    driver = webdriver.Chrome("/Users/admin/chromedriver")

    #Email
    email = "test@test.com"

    #Open Teachable
    driver.get("https://takehome.zeachable.com")

    #implicit wait
    driver.implicitly_wait(0.5)

    #maximize browser
    driver.maximize_window()

    #Click login page
    commands.loginButton(driver)

    #Check Forgot Password
    driver.find_element(by=By.XPATH, value='/html/body/main/div/form/div[3]/div[2]/a').click()

    #Validate Email Entry
    driver.find_element(by=By.NAME, value = 'email').send_keys("!!!!!!", Keys.TAB)  
    commands.checkInvalidEntry("email", "!!!!!!", driver)

    #Enter Correct Email
    driver.find_element(by=By.NAME, value = 'email').clear()
    driver.find_element(by=By.NAME, value = 'email').send_keys(email, Keys.TAB)  
    driver.find_element(by=By.NAME, value = 'commit').click()

    #implicit wait
    driver.implicitly_wait(2)

    #Validate Email Entry by checking for 'Resend Email' button 
    driver.find_element(by=By.CLASS_NAME, value = 'recaptcha-protected')

    driver.close()

except Exception as err:
    print('Selenium script failed : ', err.__class__, "occurred.")