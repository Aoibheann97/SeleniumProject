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

    #Open Teachable
    driver.get("https://takehome.zeachable.com")

    #implicit wait
    driver.implicitly_wait(0.5)

    #maximize browser
    driver.maximize_window()

    #Click login page
    commands.loginButton(driver)

    #Blank Username / Password
    commands.loginUser("", "", driver, False)

    #Incorrect Username
    commands.loginUser("!!!!!!!!", "", driver, False)

    #Clear
    driver.find_element(by=By.NAME, value = 'email').clear()

    #Wrong email & password
    commands.loginUser("test@test.com", "WrongPassword", driver, False)

    #clear
    driver.find_element(by=By.NAME, value = 'email').clear()
    driver.find_element(by=By.NAME, value = 'password').clear()

    #Correct Username / Password - Remember Me - False
    commands.loginUser("takehome@test.com", "Teachable", driver, True, False)

    #Logout
    commands.logout(driver)

    #Refresh page and ensure login isn't saved
    driver.refresh()
    driver.implicitly_wait(2)
    commands.loginButton(driver)

    #Check Remember me - Correct Username / Password - Remember Me - True
    commands.loginUser("takehome@test.com", "Teachable", driver, True, True)

    #New Tab
    driver.execute_script('''window.open("https://takehome.zeachable.com","_blank");''')
    time.sleep(2)

    #Ensure User is still logged in
    if not driver.find_element(by=By.ID, value = 'search-course-button'):
        raise Exception("User needs to log in twice in one browser session")

    #Close Window
    driver.close()

except Exception as err:
    print('Selenium script failed : ', err.__class__, "occurred.")

