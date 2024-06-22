from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try:

    driver.get("https://www.instagram.com/guviofficial/")
    time.sleep(3)
    followers_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button/span/span')
    following_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[3]/div/button/span/span')
    followers_count = followers_element.text
    following_count = following_element.text

    print("Followers:", followers_count)
    print("Following:", following_count)

finally:

    driver.quit()