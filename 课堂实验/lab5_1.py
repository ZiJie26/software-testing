from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 创建一个Firefox浏览器实例
driver = webdriver.Firefox()

# 步骤1: 打开'http://localhost/upload/message.php'，等待3秒
driver.get("http://localhost/upload/message.php")
time.sleep(3)

# 步骤2: 把浏览器窗口大小设置为宽度800px和高度600px，等待3秒
driver.set_window_size(800, 600)
time.sleep(3)

# 步骤3: 打印窗口左上角位置坐标
window_position = driver.get_window_position()
print("窗口左上角位置坐标:", window_position)

# 步骤4: 把浏览器窗口最小化，等待3秒，打印窗口大小尺寸
driver.minimize_window()
time.sleep(3)
window_size_after_minimize = driver.get_window_size()
print("窗口大小尺寸（最小化后）:", window_size_after_minimize)

# 步骤5: 自定义浏览器窗口位置，把窗口左上角坐标设置为（60px,60px），等待3秒，打印自定义后窗口左上角位置坐标
driver.set_window_position(60, 60)
time.sleep(3)
custom_window_position = driver.get_window_position()
print("自定义后窗口左上角位置坐标:", custom_window_position)

# 步骤6: 把浏览器窗口最大化，等待3秒，打印窗口大小尺寸
driver.maximize_window()
time.sleep(3)
window_size_after_maximize = driver.get_window_size()
print("窗口大小尺寸（最大化后）:", window_size_after_maximize)

# 步骤7: 点击“高级搜索”，等待3秒
driver.find_element(By.XPATH,'//*[@id="searchForm"]/a').click()
time.sleep(3)

# 步骤8: 后退，等待3秒
driver.back()
time.sleep(3)

# 步骤9: 获取当前网页的标题和URL，并打印
current_title = driver.title
current_url = driver.current_url
print("当前网页标题:", current_title)
print("当前网页URL:", current_url)

# 步骤10: 前进，等待3秒
driver.forward()
time.sleep(3)

# 步骤11: 在地址栏输入获取的URL网址进行访问，等待3秒
driver.get(current_url)
time.sleep(3)

# 步骤12: 后退，等待3秒
driver.back()
time.sleep(3)

# 步骤13: 关闭浏览器
driver.quit()
