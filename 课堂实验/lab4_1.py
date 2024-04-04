from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
driver.implicitly_wait(3)
driver.get('http://localhost/upload/index.php')
driver.find_element(By.CSS_SELECTOR, '#mainNav > a:nth-child(10)').click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(8) > div.AreaR > div:nth-child(6) > div > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input').send_keys('vip@163.com')
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(8) > div.AreaR > div:nth-child(6) > div > div > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input[type=radio]:nth-child(3)').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(8) > div.AreaR > div:nth-child(6) > div > div > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input').send_keys('维修')
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(8) > div.AreaR > div:nth-child(6) > div > div > form > table > tbody > tr:nth-child(5) > td:nth-child(2) > textarea').send_keys('手机坏了怎么处理？')
driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(8) > div.AreaR > div:nth-child(6) > div > div > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > input.bnt_blue_1').click()
sleep(1)
driver.quit()