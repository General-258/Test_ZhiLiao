# -*-coding:utf-8 -*-
#截图
from selenium import webdriver
from utils.config import REPORT_PATH
from utils.log import logger
import time
#定义截图函数,第二个参数是截图的名称
def Cut_img(driver, imgname):
    base_path = REPORT_PATH + '\\screenshot\\'  #截图保存的路径
    file_time = time.strftime("%Y%m%d_%H_%M", time.localtime(time.time()))
    screen_name = base_path + imgname + '_' + file_time  +'.png'
    screen_name = screen_name.replace('\\', '/')
    try:
        driver.get_screenshot_as_file(screen_name)
        logger.info("开始截图并保存")

    except Exception as e:
        logger.error("出现异常", format(e))
if __name__ =='__main__':
    driver = webdriver.Firefox()
    driver.get("http://192.168.1.63:8080/login.html")
    Cut_img(driver, 'bbb')
    driver.quit()