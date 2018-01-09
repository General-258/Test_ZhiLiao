# -*- coding:utf-8 -*-
import unittest, sys
from ..page.loginPage import LoginPage
from ..page.homePage import HomePage
from selenium import webdriver
sys.path.append("../utils")
from utils.config import Config,DATA_PATH
from utils.xml_reader import GetXMLTestData
from utils.log import logger
from utils import screenshot
import time

class loginTest(unittest.TestCase):
    '''登录功能测试用例'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = Config().getconf('Login_URL')  # 登录地址
        self.data_login_file = DATA_PATH + '/'+ Config().getconf('Test_Data')   # 测试数据文件地址

    # def test_login_A1(self):
    #     '''使用不存在的用户名登录'''
    #     loginpage = LoginPage(self.driver, self.url, u'知了背调-国内首款在线授权的背景调查平台')
    #     account_number = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 0, 'username')
    #     password = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 0 ,'password')
    #     loginpage.test_login(account_number, password)
    #     time.sleep(0.5)
    #     self.assertEqual(loginpage.get_prompt_text(), "您的用户名未注册，请注册后登录")
    #     logger.debug(loginpage.get_prompt_text())
    #
    # def test_login_A2(self):
    #     '''使用错误的密码登录'''
    #     loginpage = LoginPage(self.driver, self.url, u'知了背调-国内首款在线授权的背景调查平台')
    #     account_number = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 1, 'username')
    #     password = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 1, 'password')
    #     loginpage.test_login(account_number, password)
    #     time.sleep(0.5)
    #     self.assertEqual(loginpage.get_prompt_text(), "用户名与密码不匹配，请重新输入")
    #     logger.debug(loginpage.get_prompt_text())

    def test_login_A3(self):
        '''账户只有一个公司登录，成功登录'''
        loginpage = LoginPage(self.driver, self.url, u'知了背调-国内首款在线授权的背景调查平台')
        account_number = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 2, 'username')
        password = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 2, 'password')
        loginpage.test_login(account_number, password)
        time.sleep(0.5)
        self.assertEqual(HomePage.get_phone_number_text(self), account_number)

    # def test_login_1(self):
    #
    #     login_page = LoginPage(self.driver, self.url, u'登录-知了背调')
    #     a = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 0, 'username')
    #     b = GetXMLTestData().getxmlattribute(self.data_login_file, 'user', 0, 'password')
    #     login_page.user_password_login(a, b)
    #     try:
    #         self.assertEqual(login_page.get_input_error(), "账号不能为空")
    #         logger.debug(login_page.get_input_error())
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()