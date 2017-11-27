# -*- coding:utf-8 -*-
import unittest, sys
from ..page.loginPage import LoginPage
from selenium import webdriver
sys.path.append("../utils")
from utils.config import Config,DATA_PATH
from utils.xml_reader import GetXMLTestData
from utils.log import logger
from utils import screenshot
import os
import time
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))


class loginTest(unittest.TestCase):
    '''账号密码方式登录测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = Config().getconf('Login_URL')    #登录地址
        self.data_login_file = DATA_PATH +'/'+ Config().getconf('Test_Data')  #测试数据文件地址
    def test_login_1(self):
        '''用户名、密码为空点击登录'''
        login_page = LoginPage(self.driver, self.url, u'登录-知了背调')
        a = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 0, 'username')
        b = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 0, 'password')
        login_page.user_password_login(a, b)
        try:
            self.assertEqual(login_page.get_input_error(), "账号不能为空")
            logger.debug(login_page.get_input_error())
        except:
            screenshot.Cut_img(self.driver, "test_login_1")
            logger.error("提示与预期不一致")
    def test_login_2(self):
        '''账号正确，密码为空登录'''
        login_page = LoginPage(self.driver, self.url, u'登录-知了背调')
        a = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 1, 'username')
        b = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 1, 'password')
        login_page.user_password_login(a, b)
        try:
            self.assertEqual(login_page.get_input_error(), "密码不能为空")
            logger.debug(login_page.get_input_error())
        except:
            screenshot.Cut_img(self.driver, "test_login_2")
            logger.error("提示与预期不一致")
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()