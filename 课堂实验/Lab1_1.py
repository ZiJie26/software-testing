from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('http://localhost/upload/index.php')
driver.find_element(By.ID,'keyword').send_keys('30')
driver.find_element(By.NAME,'imageField').click()
sleep(5)
driver.quit()