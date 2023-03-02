from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Set to Headless
options = Options()
options.headless = True
options.add_argument('--window-size=1920,1200')

# Compile driver location and assign URL
URL = 'https://phook.net/forum/index.php'
DRIVER_PATH = '/pathto/chromedriver'  # <------ https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
driver.get(URL)

time.sleep(1)

# Login deets
username = ''
password = ''
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'button2').click()

time.sleep(1)

# Exception to verify login status
try:
    logout_button = driver.find_element(By.CSS_SELECTOR, "[title^='Logout']")
    print('Successfully logged in')
except NoSuchElementException:
    print('Incorrect login/password')

time.sleep(1) 

# Switch to URL based on task after login
URL_2 = ''
driver.get(URL_2)

# list of contestants
sadness = [
]

# New thread loop
for i in sadness:
    driver.get(URL_2)
    time.sleep(1)
    driver.find_element(By.ID, 'subject').send_keys(f'thread title {i[0]} v {i[1]} ~~~~') # <--- thread title
    driver.find_element(By.ID, 'message').send_keys(f'body') # <----- message body
    container = driver.find_element(By.ID, 'poll-panel')
    driver.execute_script("arguments[0].style.display = 'block';", container)
    time.sleep(1)
    driver.find_element(By.ID, 'poll_title').send_keys('poll title')
    driver.find_element(By.ID, 'poll_option_text').send_keys(f'{i[0]} \n{i[1]}')
    driver.find_element(By.NAME, 'post').click()
    time.sleep(30) 
