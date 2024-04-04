from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 创建一个Firefox浏览器实例
driver = webdriver.Firefox()

# 步骤2: 登录前台首页
driver.get('http://localhost/upload/user.php')#打开ecshop前台登录
driver.find_element(By.NAME,'username').send_keys('vip')
driver.find_element(By.NAME,'password').send_keys('vip')#找到登录的文本框，输入账号密码
driver.find_element(By.NAME,'submit').click()

# 步骤3: 点击“留言板”
guestbook_link = driver.find_element(By.XPATH, '//*[@id="mainNav"]/a[10]')
guestbook_link.click()
time.sleep(2)

# 步骤4: 定位电子邮件地址文本框
email_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[2]/td[2]/input')
email_input.send_keys(Keys.CONTROL, 'a')
email_input.send_keys(Keys.BACKSPACE)

# 步骤5: 输入电子邮件地址：vip@ecshop.com
email_input.send_keys("vip@ecshop.com")

# 步骤6: 按下Home键光标回到行首
email_input.send_keys(Keys.HOME)

# 步骤7: Shift+右箭头（→）连续点击三次，选中三个字符vip
email_input.send_keys(Keys.SHIFT + Keys.RIGHT * 3)

# 步骤8: Ctrl+c复制，到主题文本框里Ctrl+v粘贴
email_input.send_keys(Keys.CONTROL, 'c')
subject_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[4]/td[2]/input')
subject_input.send_keys(Keys.CONTROL, 'v')

# 步骤9: 到留言内容里输入“我是”、Ctrl+v粘贴，Enter回车换行
message_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[5]/td[2]/textarea')
message_input.send_keys("我是")
message_input.send_keys(Keys.CONTROL, 'v')
message_input.send_keys(Keys.ENTER)

# 步骤10: 再输入“请问有优惠码？”
message_input.send_keys("请问有优惠码？")

# 步骤11: 在主题文本框里按下回车
subject_input.send_keys(Keys.ENTER)

time.sleep(5)

# 关闭浏览器窗口
driver.quit()



























