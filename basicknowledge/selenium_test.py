# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:58:29 2020

@author: Administrator
"""



# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver import ActionChains


# browser = webdriver.Chrome()


# browser.get('http://taobao.com')
# input = browser.find_element_by_id('q')#搜索框input的id
# input.send_keys('cpu')
# input.send_keys(Keys.ENTER)#调用回车键
# wait = WebDriverWait(browser, 10)
# 页面一直循环，直到 id="myDynamicElement" 出现
# wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
# print(browser.current_url)
# print(browser.get_cookies())
# print(browser.page_source)
    

# 拖拽页面

# browser = webdriver.Chrome()
# url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to_frame('iframeResult')#找到这个frame
# # 找到要拖的对象
# source = browser.find_element_by_css_selector('#draggable')
# #造谣要拖到的位置
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# #执行
# actions.perform()
# browser.close()


from selenium import webdriver
browser = webdriver.Chrome()
browser.implicitly_wait(3) 
browser.get("http://www.zhihu.com/explore")
browser.implicitly_wait(3) 
#这里 document.body.scrollHeight来代表高度有问题，用具体二点数字就没问题
browser.execute_script('window.scrollTo(0, document.body.scrollTop)')

# browser.execute_script('alert("To Bottom")')
browser.close()


# =============================================================================
# 获取节点的信息
# =============================================================================
from selenium import webdriver

url = 'https://www.runoob.com/python/att-string-decode.html'
browser = webdriver.Chrome()
browser.get(url)
# logo = browser.find_element_by_id("c-tips-container")
# print(logo)
# print(logo.get_attribute('class'))#打印其class值
input1  = browser.find_element_by_class_name('feedback-btn feedback-btn-gray')
print(input1.text)
browser.close()


# =============================================================================
# 切换Frame
# =============================================================================

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser = webdriver.Chrome()
browser.get(url)
browser.switch_to_frame('iframeResult')

try:
    logo = browser.find_element_by_class_name('navbar-header')
except NoSuchElementException:
    print('NO LOGO')

browser.switch_to.parent_frame()
#只要类名里面包含logo
logo = browser.find_element_by_class_name('navbar-header')
print(logo)
print(logo.text)

browser.close()


# =============================================================================
# 显示等待
# =============================================================================











