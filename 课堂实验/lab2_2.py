#注册测试
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.implicitly_wait(16)#隐式等待的超时时间设置为16秒
driver.maximize_window()
driver.get('http://localhost/upload/index.php')#打开ecshop前台页面
sleep(3)
driver.find_element(By.XPATH,'//*[@id="ECS_MEMBERZONE"]/a[2]').click()
sleep(1)
driver.find_element(By.NAME,'username').send_keys('chuzijie')
sleep(1)
driver.find_element(By.NAME,'email').send_keys('chuzijie@scnu.com')
sleep(1)
driver.find_element(By.NAME,'password').send_keys('chuzijie')#找到注册的文本框，输入账号密码
sleep(1)
driver.find_element(By.NAME,'confirm_password').send_keys('chuzijie')
sleep(1)
driver.find_element(By.NAME,'extend_field1').send_keys('chuzijie@scnu.com')
sleep(1)
driver.find_element(By.NAME,'extend_field2').send_keys('12121212121')
sleep(1)
driver.find_element(By.NAME,'extend_field3').send_keys('133333131')
sleep(1)
driver.find_element(By.NAME,'extend_field4').send_keys('133333131')
sleep(1)
driver.find_element(By.NAME,'extend_field5').send_keys('133333131')
sleep(1)
s1 = Select(driver.find_element(By.NAME,'sel_question'))  # 实例化Select
s1.select_by_index(1)
sleep(1)
driver.find_element(By.NAME,'passwd_answer').send_keys('20030101')
sleep(1)
driver.find_element(By.NAME,'Submit').click()
sleep(1)
driver.quit()