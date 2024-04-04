from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import re

# 创建一个Firefox浏览器实例
driver = webdriver.Firefox()

# 步骤1: 打开首页
driver.get("http://localhost/upload/index.php")

# 步骤2: 输入关键字100，判断“搜索“按钮如果可用，点击搜索按钮，等待3秒
keyword_input = driver.find_element(By.XPATH,'//*[@id="keyword"]')
keyword_input.send_keys("100")
search_button = driver.find_element(By.XPATH,'//*[@id="searchForm"]/input[2]')
if search_button.is_enabled():
    search_button.click()
time.sleep(3)

# 步骤3: 点击搜索结果区域里的“金立 A30“的商品名称，等待3秒
product_link = driver.find_element(By.XPATH,'//*[@id="compareForm"]/div/div/div[3]/p/a')
product_link.click()
time.sleep(3)

# 步骤4: 打印默认“购买数量“文本框的当前默认值
quantity_input = driver.find_element(By.XPATH,'//*[@id="number"]')
default_quantity = quantity_input.get_attribute("value")
print("默认购买数量:", default_quantity)

# 步骤5: 获得“商品库存“的台数
stock_count = driver.find_element(By.XPATH,'//*[@id="ECS_FORMBUY"]/ul/li[1]/dd[2]')
stock_count_text = stock_count.text
# 使用正则表达式提取数字部分
stock_count_num = int(re.search(r'\d+', stock_count_text).group())
print("商品库存:", stock_count_num)

# 步骤6: 如果台数大于3台，清空“购买数量“文本框，输入3
if stock_count_num > 3:
    quantity_input.clear()
    quantity_input.send_keys("3")

# 步骤7: 判断“数据线“复选框，如果没有被选中，就点击选中它
data_line_checkbox = driver.find_element(By.XPATH,'//*[@id="spec_value_190"]')
if not data_line_checkbox.is_selected():
    data_line_checkbox.click()

# 步骤8: 判断“线控耳机“复选框，如果没有被选中，就点击选中它
earphone_checkbox = driver.find_element(By.XPATH,'//*[@id="spec_value_189"]')
if not earphone_checkbox.is_selected():
    earphone_checkbox.click()

# 步骤9: 获得此时的“商品总价“，如果是”￥6210元“，打印”总价计算正确“，否则打印”总价计算错误“。
total_price = driver.find_element(By.XPATH,'//*[@id="ECS_GOODS_AMOUNT"]')
if total_price.text == "￥6210元":
    print("总价计算正确")
else:
    print("总价计算错误")

# 关闭浏览器窗口
driver.quit()
