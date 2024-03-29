from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Create Web driver and access frontend URL with a specific userid
driver = webdriver.Chrome(service=Service("/Users/kobiben-senyor/Downloads/chromedriver_mac_arm64/chromedriver"))
user_id = "4"
driver.get('http://127.0.0.1:5001/users/get_user_data/' + user_id)
time.sleep(15)
#Locate the username according the the ID locator and print the result
user_element = driver.find_element(By.ID, "user")
print(user_element)
user_name = user_element.text
print("User name: " + user_name)
driver.quit()