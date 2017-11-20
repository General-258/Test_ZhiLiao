# -*- coding:utf-8 -*-
import unittest, sys
from ..page.loginPage import LoginPage
from selenium import webdriver
sys.path.append("../utils")
from utils.config import Config,DATA_PATH
from utils.file_reader import ExcelReader
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
        self.url = Config().getconf('Login_URL')
        self.data_login_file = DATA_PATH +'/'+ Config().getconf('Login_Test_Data')
        self.test_login_datas = ExcelReader(self.data_login_file, title_line=False).data
    def test_login_1(self):
        '''用户名、密码为空点击登录'''
        login_page = LoginPage(self.driver, self.url, u'登录-知了背调')
        login_page.user_password_login(self.test_login_datas[0][0], self.test_login_datas[0][1])
        try:
            self.assertEqual(login_page.get_input_error(), "账号不能为空")
            logger.debug(login_page.get_input_error())
        except:
            screenshot.Cut_img(self.driver, "test_login_1")
            logger.error("提示与预期不一致")
    def test_login_2(self):
        '''账号正确，密码为空登录'''
        login_page = LoginPage(self.driver, self.url, u'登录-知了背调')
        login_page.user_password_login(str(int(self.test_login_datas[1][0])), self.test_login_datas[1][1])
        try:
            self.assertEqual(login_page.get_input_error(), "密码不能为空")
            logger.debug(login_page.get_input_error())
        except:
            screenshot.Cut_img(self.driver, "test_login_2")
            logger.error("提示与预期不一致")
    def test_login_3(self):
        '''输入错误的账号，正确的密码'''
        login_page = LoginPage(self.driver, self.url, u'登录-知了背调')
        login_page.user_password_login(str(int(self.test_login_datas[2][0])), self.test_login_datas[2][1])
        try:
            self.assertEqual(login_page.get_input_error(), "您还没有注册")
            logger.debug(login_page.get_input_error())
        except:
            screenshot.Cut_img(self.driver, "login_test_3")
            logger.error("提示与预期不一致")
    def test_login_4(self):
        '''输入正确的账号，错误的密码'''
        login_page = LoginPage(self.driver, self.url, u'登录-知了背调')
        login_page.user_password_login(str(int(self.test_login_datas[3][0])), self.test_login_datas[3][1])
        try:
            self.assertEqual(login_page.get_input_error(), "输入的密码有误")
            logger.debug(login_page.get_input_error())
        except:
            screenshot.Cut_img(self.driver, "login_test_4")
            logger.error("提示与预期不一致")
    def test_login_5(self):
        '''输入正确的账号，正确的密码登录'''
        login_page = LoginPage(self.driver, self.url, u'登录-知了背调')
        login_page.user_password_login(str(int(self.test_login_datas[4][0])), self.test_login_datas[4][1])
        time.sleep(2)
        try:
            self.assertEqual(self.driver.title, "工作台-知了背调")
            logger.debug(self.driver.title)
        except:
            screenshot.Cut_img(self.driver,"login_test_5")
            logger.error("无法匹配到预期title")
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()