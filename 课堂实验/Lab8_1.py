from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# 创建一个Firefox浏览器实例
driver = webdriver.Firefox()

# 步骤1: 打开ECSHOP前台首页
driver.get("http://localhost/upload/index.php")

# 步骤2: 定位到登录按钮，然后单击
login_button = driver.find_element(By.XPATH, '//*[@id="ECS_MEMBERZONE"]/a[1]/img')
login_button.click()

# 步骤3: 鼠标移动到用户名文本框元素，然后单击
username_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input')
ActionChains(driver).move_to_element(username_input).click().perform()

# 步骤4: 在文本框里输入“vip”
username_input.send_keys("vip")

# 步骤5: 按下键盘的Tab键
username_input.send_keys(Keys.TAB)

# 步骤6: 等待2秒
time.sleep(2)

# 步骤7: 在密码文本框里输入“vip”
password_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input')
password_input.send_keys("vip")

# 步骤8: 按下键盘的Tab键
password_input.send_keys(Keys.TAB)

# 步骤9: 等待2秒
time.sleep(2)

# 步骤10: 此时当前焦点位于“立即登陆”这个元素，在这个焦点位置按下回车
login_button = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[3]/td[2]/input[3]')
login_button.send_keys(Keys.ENTER)

# 步骤11: 等待5秒
time.sleep(5)

# 步骤12: 关闭浏览器
driver.quit()
