# -*-coding:utf-8 -*-
from selenium.webdriver import Remote
from selenium import webdriver
def StartBrowser():
    '''
    启动浏览器驱动
    ##########################################################################################
    定义浏览器驱动函数StartBrowser（）函数，该函数可以进行配置，根据需要，配置测试用例再不同主机和浏览器下运行
    ##########################################################################################
    # host = '192.168.0.132:5555' #运行主机 ：端口号（默认本机：127.0.0.1:4444）
    # dc = {'browserName':'internet explorer','version':'','platfrom':'WINDOWS','javascriptEnabled':True}
    # # dc = {'browserName':'firefox','version':'','platfrom':'ANY','javascriptEnabled':True,
    'marionette':False,}#指定浏览器 （'chrome','firefox'）
    # driver = Remote(command_executor='http://' + host + '/wd/hub',
    #                 desired_capabilities=dc
    '''
    driver = webdriver.Firefox()
    return driver

if __name__ == '__main__':
    dr = StartBrowser()
    dr.get("http://192.168.1.63:8080/login.html")
    dr.quit()