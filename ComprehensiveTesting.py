# -----------------------------------------------------------------------------------
# 实验功能： 浏览器前进后退，窗口大小操作，获取文本框里的数据或获取静态文本数据并进行处理，获取按钮或复选框的状态，选中某一按钮或复选框，
#           模拟鼠标的单击、双击、右击等操作，模拟键盘的复制、粘贴、输入等操作，对弹出消息框进行确定、取消、截屏操作，切换浏览器窗口和Frame，
#           页面元素截屏操作，验证码获取操作
# 时间：     2024/4/4
# 作者：     楚梓杰
# 版本号：   Python 3.10
# 测试环境： PyCharm、Firefox、geckodriver.exe、ECShop网站、（软件包：selenium、ddddocr、Pillow）
# -----------------------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time
import ddddocr
from PIL import ImageGrab

# 初始化驱动器
driver = webdriver.Firefox()

# ---切换浏览器窗口和Frame操作,窗口大小操作,获取文本框里的数据或获取静态文本数据并进行处理---
# 打开后台页
driver.get("http://localhost/upload/admin/index.php")

# 窗口大小操作
driver.maximize_window()

# 输入用户名：admin
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/input').send_keys("admin")

# 输入密码：admin123
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/input').send_keys(
    "admin123")

# 输入万能验证码：0
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[3]/td[2]/input').send_keys("0")
time.sleep(2)

# 点击“进入管理中心”
driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/input').click()
time.sleep(2)

# 对左侧菜单栏进行截屏
driver.switch_to.frame("menu-frame")
element = driver.find_element(By.XPATH, '/html/body')
element.screenshot('MenuFrame.png')

# 点击“商品列表”
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a').click()
driver.switch_to.default_content()

# 等待3秒，对右侧商品列表区域进行截屏
time.sleep(3)
driver.switch_to.frame("main-frame")
element = driver.find_element(By.XPATH, '/html/body')
element.screenshot('MainFrame.png')

# 获取静态文本元素
text_element = driver.find_element(By.XPATH, '//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span')

# 获取静态文本数据
text = text_element.text

# 打印数据
print(text)

# 点击商品列表中“P806”一行中的查看按钮
driver.find_element(By.XPATH, '//*[@id="listDiv"]/table[1]/tbody/tr[5]/td[11]/a[1]').click()
driver.switch_to.default_content()
time.sleep(5)

# 切换到新窗口
driver.switch_to.window(driver.window_handles[-1])
# ---切换浏览器窗口和Frame操作,窗口大小操作,获取文本框里的数据或获取静态文本数据并进行处理---

# ---获取按钮或复选框的状态，选中某一按钮或复选框---
# 判断“数据线“复选框，如果没有被选中，就点击选中它
data_line_checkbox = driver.find_element(By.XPATH, '//*[@id="spec_value_168"]')
if not data_line_checkbox.is_selected():
    data_line_checkbox.click()
# ---获取按钮或复选框的状态，选中某一按钮或复选框---
time.sleep(2)

# ---页面元素截屏，验证码获取操作---
# 输入E-mail
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("a@b.com")

# 输入评论内容
driver.find_element(By.XPATH,
                    '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[4]/td[2]/textarea').send_keys(
    "It’s excellent")

# 获取验证码图片
captcha_element = driver.find_element(By.XPATH,
                                      '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/div/img')

# 将图片元素截图
captcha_element.screenshot("captcha.png")

# 读取图片文件的二进制
img_bytes = open("captcha.png", "rb").read()

# 创建ocr对象
ocr = ddddocr.DdddOcr()

# 识别验证码
captcha_text = ocr.classification(img_bytes)

# 输入正确的验证码
driver.find_element(By.XPATH,
                    '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/div/input').send_keys(
    captcha_text)
time.sleep(2)

# 点击“提交评论”按钮
driver.find_element(By.XPATH,
                    '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/input').click()
# ---页面元素截屏，验证码获取操作---

# ---浏览器前进后退,对弹出消息框进行确定、取消、截屏操作---
# 点击“加入购物车”按钮
driver.find_element(By.XPATH, '//*[@id="ECS_FORMBUY"]/ul/li[9]/a[1]/img').click()
time.sleep(5)

# 后退到上一个网页
driver.back()
time.sleep(5)

# 前进到下一个网页
driver.forward()

# 点击“删除”按钮
driver.find_element(By.XPATH, '//*[@id="formCart"]/table[1]/tbody/tr[2]/td[7]/a').click()
time.sleep(3)

# 切换到消息框
alert = driver.switch_to.alert

# 消息框截图
Image = ImageGrab.grab()
Image.save('alert.png')

# 获取消息框的文本并打印
print(alert.text)

# 点击“取消”按钮
alert.dismiss()

# 点击“删除”按钮
driver.find_element(By.XPATH, '//*[@id="formCart"]/table[1]/tbody/tr[2]/td[7]/a').click()
time.sleep(3)

# 对消息框进行确认
driver.switch_to.alert.accept()
# ---浏览器前进后退,对弹出消息框进行确定、取消、截屏操作---

# ---模拟鼠标的单击、双击、右击等操作，模拟键盘的复制、粘贴、输入等操作---
# 定位到登录按钮，然后单击
login_button = driver.find_element(By.XPATH, '//*[@id="ECS_MEMBERZONE"]/a[1]')
login_button.click()

# 鼠标移动到用户名文本框元素，然后单击
username_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input')
ActionChains(driver).move_to_element(username_input).click().perform()

# 在文本框里输入“vip”
username_input.send_keys("vip")

# 按下键盘的Tab键
username_input.send_keys(Keys.TAB)

# 等待2秒
time.sleep(2)

# 在密码文本框里输入“vip”
password_input = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input')
password_input.send_keys("vip")

# 按下键盘的Tab键
password_input.send_keys(Keys.TAB)

# 等待2秒
time.sleep(2)

# 此时当前焦点位于“立即登陆”这个元素，在这个焦点位置按下回车
login_button = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/form/table/tbody/tr[3]/td[2]/input[3]')
login_button.send_keys(Keys.ENTER)

# 等待5秒
time.sleep(5)

# 点击“留言板”
guestbook_link = driver.find_element(By.XPATH, '//*[@id="mainNav"]/a[10]')
guestbook_link.click()
time.sleep(2)

# 定位电子邮件地址文本框
email_input = driver.find_element(By.XPATH,
                                  '/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[2]/td[2]/input')
email_input.send_keys(Keys.CONTROL, 'a')
email_input.send_keys(Keys.BACKSPACE)

# 输入电子邮件地址：vip@ecshop.com
email_input.send_keys("vip@ecshop.com")
time.sleep(2)

# 按下Home键光标回到行首
email_input.send_keys(Keys.HOME)
time.sleep(2)

# hift+右箭头（→）连续点击三次，选中三个字符vip
email_input.send_keys(Keys.SHIFT + Keys.RIGHT * 3)
time.sleep(2)

# Ctrl+c复制，到主题文本框里Ctrl+v粘贴
email_input.send_keys(Keys.CONTROL, 'c')
subject_input = driver.find_element(By.XPATH,
                                    '/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[4]/td[2]/input')
subject_input.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 到留言内容里输入“我是”、Ctrl+v粘贴，Enter回车换行
message_input = driver.find_element(By.XPATH,
                                    '/html/body/div[7]/div[2]/div[4]/div/div/form/table/tbody/tr[5]/td[2]/textarea')
message_input.send_keys("我是")
message_input.send_keys(Keys.CONTROL, 'v')
message_input.send_keys(Keys.ENTER)
time.sleep(2)

# 再输入“请问有优惠码？”
message_input.send_keys("请问有优惠码？")
time.sleep(2)

# 在主题文本框里按下回车
subject_input.send_keys(Keys.ENTER)
time.sleep(5)
# ---模拟鼠标的单击、双击、右击等操作，模拟键盘的复制、粘贴、输入等操作---

# 关闭浏览器
driver.quit()
