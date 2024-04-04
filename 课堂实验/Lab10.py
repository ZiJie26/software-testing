from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 初始化驱动器
driver = webdriver.Firefox()

# 打开ECSHOP前台首页
driver.get("http://localhost/upload/index.php")

# 点击注册按钮
driver.find_element(By.XPATH, '//*[@id="ECS_MEMBERZONE"]/a[2]/img').click()
time.sleep(5)

# 点击“用户协议”
driver.find_element(By.XPATH, '/html/body/div[7]/div/form/table/tbody/tr[13]/td[2]/label/a').click()
time.sleep(8)

# 获得当前窗口句柄，保存在变量里
main_window_handle = driver.current_window_handle

# 切换到最新窗口
driver.switch_to.window(driver.window_handles[-1])

# 在新窗口里点击配送与支付按钮
driver.find_element(By.XPATH, '/html/body/div[9]/div/div/dl[3]/dt/a').click()
time.sleep(5)

# 点击“EC论坛”，切换到新窗口
driver.find_element(By.XPATH, '//*[@id="mainNav"]/a[11]').click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])

# 点击“ECShop装修市场”，切换到新窗口
driver.find_element(By.XPATH, '/html/body/div[5]/table/tbody/tr[2]/td[2]/a[2]/font').click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])

# 点击适用产品下面的“ecshop”按钮
driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/dl[1]/dd[3]/a').click()
time.sleep(3)

# 关闭“EC论坛”窗口
driver.close()

# 用前面变量里保存的句柄切换回原窗口
driver.switch_to.window(main_window_handle)

# 输入用户名“Jack”
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("Jack")
time.sleep(3)

# 关闭浏览器
driver.quit()
