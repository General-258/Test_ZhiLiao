# -*-coding:utf-8 -*-
from selenium import webdriver
from utils.config import DRIVER_PATH

CHROMEDRIVER_PATH = DRIVER_PATH +'\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
TYPES = {'firefox':webdriver.Firefox, 'chrome':webdriver.Chrome, 'ie':webdriver.Ie}
EXECUTABLE_PATH = {'fire':'wires', 'chrome': CHROMEDRIVER_PATH, 'ie':IEDRIVER_PATH}
class UnSupportBrowserTypeError(Exception):
    pass
class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ','.join(TYPES.keys()))
        self.driver = None
    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self
    def close(self):
        self.driver.close()
    def quit(self):
        self.driver.quit()


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