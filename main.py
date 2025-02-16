from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, json

locators= {
    # First site, i.e. saucedemo locators
    'first_site_username': (By.ID, 'user-name'),
    'first_site_password': (By.ID, 'password'),
    'login-button': (By.ID, 'login-button'),
    'welcome-page-header': (By.XPATH, '//div[contains(text(), "Swag Labs")]'),

    # Second site, i.e. practice-automation locators
    'second_site_username': (By.ID, 'username'),
    'second_site_password': (By.ID, 'password'),
    'submit-button': (By.ID, 'submit'),
    'login-successful': (By.XPATH, "//h1[text()='Logged In Successfully']")
}

# Read data from the credentials.json file
with open('assets/credentials.json', 'r') as file:
    data= json.load(file)

    print('Reading credentials from "credentials.json" file...\n')
    # Dump values from file to the variables
    saucedemo_username= data['saucedemo_username']
    saucedemo_password= data['saucedemo_password']
    practice_automation_username= data["practice_automation_username"]
    practice_automation_password= data["practice_automation_password"]

saucedemo_url= 'https://www.saucedemo.com'
practice_automation_url= 'https://practicetestautomation.com/practice-test-login/'

l= locators

# Initialize webdriver (I am using an external library here)
driver= webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()))

# Launch first Login url (This is the first url I hav picked for testing!)

driver.get(saucedemo_url)

wait= WebDriverWait(driver, 20, poll_frequency=1)
userNameElement= wait.until(EC.visibility_of_element_located(locators['first_site_username']))
print("Entering username: ", saucedemo_username)
userNameElement.send_keys(saucedemo_username)

passWordElement= wait.until(EC.visibility_of_element_located(locators['first_site_password']))
print("Entering password...")
passWordElement.send_keys(saucedemo_password)

loginButton= wait.until(EC.visibility_of_element_located(locators['login-button']))
print('Clicking Login button')
loginButton.click()

welcomePageHeader= wait.until(EC.visibility_of_element_located(l['welcome-page-header']))
if welcomePageHeader: print('Verified Successful Login! \n')

driver.save_screenshot('./snapshots/Login_successful_Saucedemo.png')
print('Switching to the second site now!!')

# Now second site!
driver.get(practice_automation_url)

wait= WebDriverWait(driver, 20, poll_frequency=1)
userNameElement= wait.until(EC.visibility_of_element_located(locators['second_site_username']))
print("Entering username: ", practice_automation_username)
userNameElement.send_keys(practice_automation_username)

passWordElement= wait.until(EC.visibility_of_element_located(locators['second_site_password']))
print("Entering password...")
passWordElement.send_keys(practice_automation_password)

loginButton= wait.until(EC.visibility_of_element_located(locators['submit-button']))
print("Clicking Submit Button!")
loginButton.click()

welcomePageHeader= wait.until(EC.visibility_of_element_located(l['login-successful']))
if welcomePageHeader: print('Verified Successful Login!')

driver.save_screenshot('./snapshots/Login_successful_practice_automation.png')





