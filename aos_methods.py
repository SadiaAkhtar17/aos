
import sys
import datetime
import aos_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
s = Service(executable_path='../chromedriver.exe')

driver = webdriver.Chrome(service=s)

def setUp():
    print(f'Advantage Online Shopping test started at: {datetime.datetime.now()}')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('https://advantageonlineshopping.com/#/')

    if driver.current_url == 'https://advantageonlineshopping.com/#/' and driver.title == '\xa0Advantage Shopping':
        print(f'We\'re at Advantage Online Shopping homepage:  {driver.current_url}')
        print(f'We\'re seeing title message: ', {driver.title})
        print()
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(1)
    if driver.current_url == 'https://advantageonlineshopping.com/#/register':
        driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
        sleep(1)
        driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(1)
        driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
        sleep(1)
        driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
        sleep(1)
        driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(1)
        driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(1)
        driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
        sleep(1)
        Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text('Canada')
        sleep(1)
        driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(1)
        driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(1)
        driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
        sleep(1)
        driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postalcode)
        sleep(1)
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(1)
        driver.find_element(By.ID, 'register_btnundefined').click()
        sleep(1)

def validated_new_user_created():
    if driver.current_url == locators.aos_url:
        assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
        print(f'username: {locators.new_username} is displayed')
        sleep(3)
    else:
        print(f'new user account not created, please verify your code')


def log_in():
    if driver.current_url == locators.aos_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(4)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(1)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(1)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        print(f'Log in successfully done. \n'f'We logged in with Username')
    else:
        print(f'Login not successful, please verify you login credentials')


def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(1)
    if driver.current_url == locators.aos_url:
        print(f'User Log out successfully done at: {datetime.datetime.now()}')
    else:
        print(f'unable to log out')


def validated_user_login():
    if driver.current_url == locators.aos_url:
        assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
        print(f'Expected user: {locators.new_username} login successful')
        sleep(1)
    else:
        print(f'User not login, please verify your code')



# setUp()
#
# create_new_user()
#
# validated_new_user_created()
#
# log_out()
#
# log_in()
#
# validated_user_login()
#
# log_out()
#
# tearDown()
