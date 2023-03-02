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
DRIVER_PATH = '/chromedriver_mac64/chromedriver'
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
driver.get("https://phook.net/forum/posting.php?mode=post&f=3")

# list of contestants
sadness = [
    ['1 cgris', '16 fook'],
    ['8 blee', '9 bees'],
    ['5 mbg', '12 boobless'],
    ['4 briank', '13 crack'],
    ['6 suprisevalleywsp', '11 babydonkey'],
    ['3 amishbob', '14 feenom'],
    ['7 bearcobb', '10 bjk'],
    ['2 jbs', '15 mattpanic1'],
    ['1 joe_', '16 moose'],
    ['8 deadgator', '9 joonze'],
    ['5 ren', '12 januszak'],
    ['4 cpj', '13 giddy'],
    ['6 eight', '11 bluelawn'],
    ['3 antelope5', '14 ILL'],
    ['7 elroy', '10 boots'],
    ['2 jcbstan', '15 hermit'],
    ['1 sand', '16 pooks'],
    ['8 sticky-sweet', '9 ericpotato'],
    ['5 shamus', '12 maki'],
    ['4 hobbs', '13 pyrrh'],
    ['6 schof', '11 jakqlin'],
    ['3 jancy', '14 mid'],
    ['7 secondtube', '10 cactus'],
    ['2 jibs', '15 pish'],
    ['1 trout', '16 warpar'],
    ['8 treef', '9 halyem'],
    ['5 yoyo', '12 sycho'],
    ['4 gratefuldad', '13 toda'],
    ['6 phishingruven', '11 knotesau'],
    ['3 menudo', '14 simonie'],
    ['7 milliways', '10 flounder'],
    ['2 kbd', '15 rdf']
]

# CREATE NEW THREAD
for i in sadness:
    driver.get("https://phook.net/forum/posting.php?mode=post&f=3")
    time.sleep(1)
    driver.find_element(By.ID, 'subject').send_keys(f'thread title {i[0]} v {i[1]} ~~~~') # <--- thread title
    driver.find_element(By.ID, 'message').send_keys(f'body') # <----- message body
    container = driver.find_element(By.ID, 'poll-panel')
    driver.execute_script("arguments[0].style.display = 'block';", container)
    time.sleep(1)
    driver.find_element(By.ID, 'poll_title').send_keys('sadness showdown')
    driver.find_element(By.ID, 'poll_option_text').send_keys(f'{i[0]} \n{i[1]}')
    driver.find_element(By.NAME, 'post').click()
    time.sleep(30) 
