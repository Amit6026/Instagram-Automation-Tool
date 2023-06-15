import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import requests
import bs4


import os
import wget

Path = "path of your chrome driver"


driver = webdriver.Chrome(Path)

url = "https://www.instagram.com/"

driver.get(url)

username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))
)
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))
)

username.clear()
username.send_keys("your instagram account name")
password.clear()
password.send_keys("your password")


# time.sleep(2)

login = (
    WebDriverWait(driver, 10)
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    .click()
)
alert = (
    WebDriverWait(driver, 15.00)
    .until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Not now")]')))
    .click()
)
time.sleep(1)
alert2 = (
    WebDriverWait(driver, 15.00)
    .until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))
    )
    .click()
)
profile = (
    WebDriverWait(driver, 15.00)
    .until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Profile")]')))
    .click()
)
# followers = (
#     WebDriverWait(driver, 10.00)
#     .until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '//a[href="/divinebulls50/followers/"]'))
#     )
#     .click()
# )
# print(followers)



time.sleep(10)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a').click()

time.sleep(10)

# followers = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div')

followers = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div')
print(followers)


for x in followers:
 print(x)


input("wait!")
