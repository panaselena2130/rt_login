import time

from selenium import webdriver
from  selenium.webdriver.common.by import By

web_element = webdriver.Chrome()
web_element.maximize_window()
web_element.get('https://rt-students.xyz:3042/#/login')
time.sleep(2)

username = 'pa********.ru'
name = web_element.find_element(By.XPATH, '//*[@id="mat-input-0"]')
name.send_keys(username)
time.sleep(2)

user_password='3*********'
password=web_element.find_element(By.XPATH, '//*[@id="mat-input-1"]')
password.send_keys(user_password)
time.sleep(2)


login_element = web_element.find_element(By.XPATH,'/html/body/app-root/div[1]/div[2]/login-cmp/div/div/div/div/div/div[2]/button').click()
time.sleep(2)



