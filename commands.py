from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def loginButton(driver):
    driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div/div/div/ul/li[1]/a').click()
    #Pause
    time.sleep(2)

def logout(driver):
    driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div/div/div/ul/li[3]/a/img').click()
    time.sleep(2)
    driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div/div/div/ul/li[3]/ul/li[6]/a').click()
    #Pause
    time.sleep(2)

def checkInvalidEntry(elementValue, inputValue, driver):
    time.sleep(2)
    #Expect red border when invalid password
    expectedColour = "rgb(204, 0, 0)"

     #Error Message for required field
    if elementValue == "email" and not '@' in inputValue and not inputValue == "":
        errorMessage = "Please provide a valid email address"
    else:
        errorMessage = 'This field is required'

    #Define element
    borderElement = driver.find_element(by=By.NAME, value = elementValue)

    #Actual colour
    obtainedColour = borderElement.value_of_css_property('border-color')

    #Check Obtained colour is Red(expected)
    if not obtainedColour == expectedColour:
        raise Exception("expected colour is {expectedColour} and got {obtainedColour}")

    #Verify Error
    VerifyError("inline-error", errorMessage, driver)


def loginUser(email, password, driver, valid, rememberMe=False):

    time.sleep(2)

    #Input Email
    driver.find_element(by=By.NAME, value = 'email').send_keys(email, Keys.TAB)
    if valid == False and not '@' in email:
        checkInvalidEntry("email", email, driver)

    #Input Password
    driver.find_element(by=By.NAME, value = 'password').send_keys(password, Keys.TAB)
    if valid == False and password == "":
        checkInvalidEntry("password", password, driver)

    #Remember Me Checkbox
    if not rememberMe and driver.find_element(by=By.ID, value = 'remember_me').get_attribute("checked"):
            driver.find_element(by=By.ID, value = 'remember_me').click()

    #Click Submit
    driver.find_element(by=By.NAME, value = 'commit').click()
    time.sleep(3)

    #Check if login was successful/unsuccessful
    if valid:
        if not driver.find_element(by=By.ID, value = 'search-course-button'):
            raise Exception("Login not Successful")
    else:
        VerifyError("flash-error", "Login Unsuccessful Error Message hasn't appeared", driver)


def signupUser(fullName, email, password, driver, emailInUse, valid, allowMarketing=False):

    time.sleep(2)

    #Input Full Name
    driver.find_element(by=By.ID, value = 'user_name').send_keys(fullName, Keys.TAB)
    if valid == False:
        checkInvalidEntry("name", email, driver)

    #Input Email
    driver.find_element(by=By.ID, value = 'user_email').send_keys(email, Keys.TAB)
    if valid == False and not '@' in email:
        checkInvalidEntry("email", email, driver)

    #Input Password
    driver.find_element(by=By.ID, value = 'password').send_keys(password, Keys.TAB)
    if valid == False and password == "":
        checkInvalidEntry("password", password, driver)

    #Remember Me Checkbox
    if not allowMarketing and driver.find_element(by=By.ID, value = 'allow_marketing_emails').get_attribute("checked"):
            driver.find_element(by=By.ID, value = 'allow_marketing_emails').click()

    #Click Submit
    driver.find_element(by=By.NAME, value = 'commit').click()
    time.sleep(3)

    #Check if signup was successful/unsuccessful
    if valid:
        if emailInUse:
            VerifyError("flash-error", "Email is already in use. Please log in to your account.", driver)
        elif not driver.find_element(by=By.ID, value = 'search-course-button'):
            raise Exception("Signup not Successful")
    else:
        VerifyError("page-error", "Our apologies! We were unable to process your request", driver)


def VerifyError(type, errorMessage, driver):
    errors = driver.find_elements(by=By.CLASS_NAME,value=type)
    if not (errorMessage in e.text for e in errors):
        raise Exception("Unsuccessful - Expected Error Message hasn't appeared")