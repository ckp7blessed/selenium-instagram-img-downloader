from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget
import time

pwx = ''
username = ''

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.instagram.com/')

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys(username)
password.send_keys(pwx)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
keyword = '#motivational'
searchbox.send_keys(keyword)
time.sleep(1)
searchbox.send_keys(Keys.ENTER)
searchbox.send_keys(Keys.ENTER)

time.sleep(3)
driver.execute_script('window.scrollTo(0,1);')

images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
print(images)

# CREATING A NEW DIRECTORY FOLDER

path = 'C:/Users/Boss/Desktop//ig_ws'
count = os.listdir('C:\\Users\\Boss\\Desktop\\ig_ws')

counter = len(count) +1
for image in images:
    save_as = os.path.join(path, 'ig_ws' + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1