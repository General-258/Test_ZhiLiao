# -*- coding:utf-8 -*-
from time import sleep
import unittest, sys
sys.path.append("./Model")
sys.path.append("./PageObject")
from page.loginPage import LoginPage
from PageObject.faQiBeiDiaoPage import FaQiBeiDiaoPage
from selenium import webdriver
from time import sleep


class loginTest(unittest.TestCase):
    '''发起背调测试'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.url = "http://192.168.1.63:8080/login.html"
    def test_bei_diao_1(self):
        '''从工作台成功进入输入三要素页面'''
        loginpage = LoginPage(self.driver, self.url, u'登录-知了背调')
        loginpage.user_password_login('17717564981', '1234qwer')
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.click_start_reference_check()
        self.assertEqual(faqipage.get_fa_qi_bei_diao_text(), '填写信息')
    def test_bei_diao_2(self):
        '''姓名输入为空，然后去输入身份证号'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.click_input_name()
        faqipage.click_input_id_number()
        self.assertEqual(faqipage.get_input_error_text(), '姓名不能为空')
    def test_bei_diao_3(self):
        '''身份证输入为空，然后去输入手机号'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.click_input_id_number()
        faqipage.click_input_phone_number()
        self.assertEqual(faqipage.get_input_error_text(), '身份证不能为空')
    def test_bei_diao_4(self):
        '''先输手机号，不输入点击输入身份证号'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.click_input_phone_number()
        faqipage.click_input_id_number()
        self.assertEqual(faqipage.get_input_error_text(), '手机号不能为空')
    def test_bei_diao_5(self):
        '''姓名输入格式错误，去输入身份证号'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.input_name('123')
        faqipage.click_input_id_number()
        self.assertEqual(faqipage.get_input_error_text(), '姓名输入有误')
    def test_bei_diao_6(self):
        '''姓名输入正确，输入错误身份证，然后去输手机号'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.input_name('靳生顺')
        faqipage.input_phone_number('iii')
        faqipage.click_input_phone_number()
        self.assertEqual(faqipage.get_input_error_text(), '身份证号输入有误')
    def test_bei_diao_7(self):
        '''姓名输入正确，去输入身份证'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.input_name('靳生顺')
        faqipage.click_input_id_number()
        self.assertEqual(faqipage.get_input_error_text(), '姓名格式正确')
    def test_bei_diao_8(self):
        '''姓名输入正确，身份证号输入正确，去输入手机号'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.input_name('靳生顺')
        faqipage.input_id_number('632124199210262815')
        faqipage.click_input_phone_number()
        self.assertEqual(faqipage.get_input_error_text(), '身份证格式正确')
    def test_bei_diao_9(self):
        '''姓名输入正确，省份证号码输入正确，手机号格式错误'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.input_name('靳生顺')
        faqipage.input_id_number('632124199210262815')
        faqipage.input_phone_number('1771756498')
        faqipage.input_department('')
        self.assertEqual(faqipage.get_input_error_text(), '手机号输入有误')
    def test_bei_diao_10(self):
        '''三要素不输入，点击发起背调'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.user_password_success_login('17717564981', '1234qwer')
        faqipage.click_start_button()
        self.assertEqual(faqipage.get_input_error_text(), '三要素输入有误')
    def test_bei_diao_11(self):
        '''三要素任意一项不输入，点击发起背调'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.input_name('靳生顺')
        faqipage.input_id_number('632124199210262815')
        faqipage.click_start_button()
        self.assertEqual(faqipage.get_input_error_text(), '三要素输入有误')
    def test_bei_diao_12(self):
        '''身份证号和姓名不匹配，点击发起背调'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.input_name('靳生顺')
        faqipage.input_id_number('632124199210262816')
        faqipage.input_phone_number('17717564981')
        faqipage.click_start_button()
        self.assertEqual(faqipage.get_san_yao_su_error_text(), '身份证和姓名输入不匹配，请确认输入是否有误')
    def test_bei_diao_13(self):
        '''身份证和姓名匹配，电话号码不匹配，进入人工审核'''
        faqipage = FaQiBeiDiaoPage(self.driver, self.url, u'登录-知了背调')
        faqipage.input_name('靳生顺')
        faqipage.input_id_number('632124199210262815')
        faqipage.input_phone_number('17717564982')
        faqipage.click_start_button()
        print faqipage.get_ren_gong_text()
        # 这里需要截图
        faqipage.click_ren_gong_next()
        # 截图




    def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()