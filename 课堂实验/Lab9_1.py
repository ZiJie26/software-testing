import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 初始化驱动器
driver = webdriver.Firefox()

# 打开ECSHOP前台首页
driver.get("http://localhost/upload/index.php")

# 点击“搜索”按钮
driver.find_element(By.XPATH, '//*[@id="searchForm"]/input[2]').click()
time.sleep(3)

# 切换到消息框
alert = driver.switch_to.alert

# 获取消息框的文本并打印
print(alert.text)

# 点击“确定”按钮
alert.accept()

# 在关键字文本框中输入“806”
driver.find_element(By.XPATH, '//*[@id="keyword"]').send_keys("806")

# 点击“搜索”按钮
driver.find_element(By.XPATH, '//*[@id="searchForm"]/input[2]').click()
time.sleep(3)

# 点击P806商品名称
driver.find_element(By.XPATH, '//*[@id="compareForm"]/div/div/div/p/a').click()
time.sleep(3)

# 点击“加入购物车”按钮
driver.find_element(By.XPATH, '//*[@id="ECS_FORMBUY"]/ul/li[9]/a[1]/img').click()
time.sleep(6)

# 点击“删除”按钮
driver.find_element(By.XPATH, '//*[@id="formCart"]/table[1]/tbody/tr[2]/td[7]/a').click()
time.sleep(3)

# 切换到消息框
alert = driver.switch_to.alert

# 获取消息框的文本并打印
print(alert.text)

# 点击“取消”按钮
alert.dismiss()

# 关闭浏览器
driver.quit()
