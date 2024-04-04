from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 初始化驱动器
driver = webdriver.Firefox()

# 打开后台页
driver.get("http://localhost/upload/admin/index.php")

# 输入用户名：admin
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys("admin")

# 输入密码：admin123
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys("admin123")

# 输入万能验证码：0
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input').send_keys("0")

# 等待3秒，进行截屏
time.sleep(3)
driver.save_screenshot('screenshot1.png')

# 点击“进入管理中心”
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input').click()
time.sleep(3)

# 等待5秒，进行截屏
time.sleep(5)
driver.save_screenshot('screenshot2.png')

# 对左侧菜单栏进行截屏
driver.switch_to.frame("menu-frame")
element = driver.find_element(By.XPATH, '/html/body')
element.screenshot('screenshot3.png')

# 点击“商品列表”
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a').click()
driver.switch_to.default_content()

# 等待3秒，对右侧商品列表区域进行截屏
time.sleep(3)
driver.switch_to.frame("main-frame")
element = driver.find_element(By.XPATH, '/html/body')
element.screenshot('screenshot4.png')

# 点击商品列表中“夏新N7”一行中的查看按钮
driver.find_element(By.XPATH, '/html/body/form/div[1]/table[1]/tbody/tr[11]/td[11]/a[1]').click()
driver.switch_to.default_content()

# 等待3秒，切换到新窗口，对新窗口进行截屏
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.save_screenshot('screenshot5.png')

# 点击登录按钮
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/font/a[1]').click()

# 等待3秒，进行截屏
time.sleep(3)
driver.save_screenshot('screenshot6.png')

# 点击“立即登陆”按钮
driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[3]/td[2]/input[3]').click()

# 等待2秒，进行截屏
time.sleep(2)

# 对消息框进行确认
driver.switch_to.alert.accept()

# 输入用户名：vip
driver.find_element(By.NAME,'username').send_keys('vip')

# 输入密码：vip
driver.find_element(By.NAME,'password').send_keys('vip')

# 点击“立即登陆”按钮
driver.find_element(By.NAME,'submit').click()

# 等待3秒，进行截屏
time.sleep(3)
driver.save_screenshot('screenshot8.png')

# 自动刷新页面后，对包含ECSHOP图标在内的最上侧区域进行截屏
element = driver.find_element(By.XPATH, '/html/body/div[1]')
element.screenshot('screenshot9.png')

# 关闭浏览器
driver.quit()
