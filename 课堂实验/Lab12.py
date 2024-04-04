from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

# 点击界面上方“个人设置”
driver.switch_to.frame("header-frame")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/ul/li[6]/a').click()
time.sleep(5)
driver.switch_to.default_content()

# 选中“设置个人导航”右侧下拉列表的从第1个到第6个选项
driver.switch_to.frame("main-frame")
select = Select(driver.find_element(By.XPATH, '//*[@id="all_menu_list"]'))
for i in range(0, 7):
    select.select_by_index(i)
time.sleep(5)

# 取消文本是“商品管理”的选项，取消第2个选项，取消value是”comment_manage.php?act=list”的选项
select.deselect_by_visible_text('商品管理')
select.deselect_by_index(2)
select.deselect_by_value('comment_manage.php?act=list')
time.sleep(5)

# 取消右侧下拉列表所有选项
select.deselect_all()

# 选择右侧文本是“商品类型”的选项
select.select_by_visible_text('    商品类型')
time.sleep(3)

# 如果“增加”按钮变为可用，点击它
add_button = driver.find_element(By.XPATH, '//*[@id="btnAdd"]')
if add_button.is_enabled():
    add_button.click()
time.sleep(5)

# 选中“设置个人导航”左侧下拉列表的最后一个选项和倒数第二个选项
select = Select(driver.find_element(By.XPATH, '//*[@id="menus_navlist"]'))
select.select_by_index(len(select.options) - 1) # 倒数第一用长度-1
select.select_by_index(len(select.options) - 2)
time.sleep(3)

# 打印左侧下拉列表中所有已被选中的选项的文本
selected_options = select.all_selected_options
for option in selected_options:
    print(option.text)

# 打印左侧下拉列表中已被选中的选项中第一个的文本
print(selected_options[0].text)

# 关闭浏览器
driver.quit()
