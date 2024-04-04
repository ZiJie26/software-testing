from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import ddddocr

# 初始化驱动器
driver = webdriver.Firefox()

# 打开ECShop前台P806商品详情页
driver.get("http://localhost/upload/goods.php?id=24")

# 输入E-mail
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("a@b.com")

# 输入评论内容
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[4]/td[2]/textarea').send_keys("It’s excellent")

# 获取验证码图片
captcha_element = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/div/img')

# 将图片元素截图
captcha_element.screenshot("captcha.png")

# 读取图片文件的二进制
img_bytes = open("captcha.png", "rb").read()

# 创建ocr对象
ocr = ddddocr.DdddOcr()

# 识别验证码
captcha_text = ocr.classification(img_bytes)

# 输入正确的验证码
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/div/input').send_keys(captcha_text)

# 点击“提交评论”按钮
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[9]/div[1]/div/div/div[3]/form/table/tbody/tr[5]/td/input').click()

# 关闭浏览器
driver.quit()
