from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 初始化驱动器
driver = webdriver.Firefox()

# 一、文件上传
# 打开ECShop前台登录页
driver.get("http://localhost/upload/user.php")

# 输入用户名：vip
driver.find_element(By.NAME,'username').send_keys('vip')

# 输入密码：vip
driver.find_element(By.NAME,'password').send_keys('vip')

# 点击“立即登陆”按钮
driver.find_element(By.NAME,'submit').click()
time.sleep(5)

# 点击上方“用户中心”
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/font/font/a[1]').click()
time.sleep(3)

# 点击左侧“我的留言”
driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div/div/div/a[6]').click()
time.sleep(3)

# 输入主题“hello”
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[2]/td[2]/input').send_keys("hello")

# 输入留言内容“welcome to this world!”
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[3]/td[2]/textarea').send_keys("welcome to this world!")

# 选择文件c:\\temp\\777.txt
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[4]/td[2]/input').send_keys("c:\\\\temp\\\\777.txt")

# 点击“提交”
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div/form/table/tbody/tr[5]/td[2]/input[2]').click()

# 二、文件下载
# 打开网页
driver.get("http://sahitest.com/demo/saveAs.htm")

# 下载testsaveas.zip文件
driver.find_element(By.XPATH, '/html/body/a[1]').click()

# 关闭浏览器
driver.quit()
