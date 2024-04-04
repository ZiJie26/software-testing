#登录测试
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver=webdriver.Firefox()
driver.implicitly_wait(16)#隐式等待的超时时间设置为16秒
driver.maximize_window()
driver.get('http://localhost/upload/user.php')#打开ecshop前台登录
sleep(3)
driver.find_element(By.NAME,'username').send_keys('vip')
driver.find_element(By.NAME,'password').send_keys('vip')#找到登录的文本框，输入账号密码
driver.find_element(By.NAME,'submit').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="ECS_MEMBERZONE"]/font/a[1]').click()
sleep(2)
driver.find_element(By.XPATH,'/html/body/div[7]/div[1]/div/div/div/div/a[2]').click()
sleep(5)
driver.quit()
