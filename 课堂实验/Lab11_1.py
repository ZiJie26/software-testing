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

# 点击“进入管理中心”
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input').click()
time.sleep(3)

# 点击左侧菜单里的“商品列表”
driver.switch_to.frame("menu-frame")
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a').click()
time.sleep(5)

# 在frame中的操作完成后要切换到主内容区
driver.switch_to.default_content()

# 点击商品名称为“诺基亚N85”一行后面的“查看”操作按钮
driver.switch_to.frame("main-frame")
driver.find_element(By.XPATH, '/html/body/form/div[1]/table[1]/tbody/tr[3]/td[11]/a[1]').click()
time.sleep(5)

# 切换到新的窗口
driver.switch_to.window(driver.window_handles[-1])

# 判断“蓝牙耳机”前的复选框是否选中，若否，选中复选框
checkbox = driver.find_element(By.XPATH, '//*[@id="spec_value_158"]')
if not checkbox.is_selected():
    checkbox.click()

# 点击“加入收藏夹”按钮
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[2]/form/ul/li[9]/a[2]/img').click()
time.sleep(5)

# 若有弹窗，点击“确定”
try:
    driver.switch_to.alert.accept()
except:
    pass

# 关闭“诺基亚N85”窗口
driver.close()

# 切换回原窗口
driver.switch_to.window(driver.window_handles[0])

# 点击左侧菜单里的“商品回收站”
driver.switch_to.frame("menu-frame")
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[1]/ul/li[7]/a').click()
time.sleep(5)
driver.switch_to.default_content()

# 点击上方“开店向导”按钮
driver.switch_to.frame("header-frame")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/ul/li[9]/a').click()
time.sleep(5)

# 点击“退出”
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/a[2]').click()
time.sleep(5)
driver.switch_to.default_content()

# 输入管理员姓名：Jack
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys("Jack")

# 关闭浏览器
driver.quit()
