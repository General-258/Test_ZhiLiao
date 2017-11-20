# -*-coding:utf-8 -*-
#截图
from selenium import webdriver
import os

#定义截图函数
def Cut_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))#该脚本运行的绝对路径;
    base_dir = str(base_dir)   #转为字符串
    base_dir = base_dir.replace('\\','/')#字符串替换;'E:/oldTest/CaseDataReport/TestCase/Model'
    base = base_dir.split('TestCase')[0]
    print base
    file_path = base + 'Report/image/'+file_name
    driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.1.63:8080/login.html")
    Cut_img(driver,'63.jpg')
    driver.quit()