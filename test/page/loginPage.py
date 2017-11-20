# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase
from time import sleep


class LoginPage(PageBase):
    password_login_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[1]/div[1]")
    account_number_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[2]/div[1]/input")
    password_loc = (By.ID, "mm")
    login_password_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[2]/div[4]/div")
    verify_login_loc = (By.CLASS_NAME, "html/body/div[2]/div[2]/div/div/div[1]/div[2]")
    phone_number_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[3]/div[1]/input")
    get_verify_code_loc = (By.ID, "hqyzm")
    input_verify_code_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[3]/div[2]/input")
    login_verify_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[3]/div[3]/div")
    alert_error_loc = (By.XPATH, "html/body/div[7]/div/p")

    # 打开页面
    def open(self):
        self._open(self.base_url, self.page_title)

    # 点击选择用账号密码登录
    def click_password_login(self):
        self.find_element(*self.password_login_loc).click()

    # 输入账号
    def input_account_number(self, account_number):
        self.find_element(*self.account_number_loc).clear()
        self.find_element(*self.account_number_loc).send_keys(account_number)

    # 输入密码
    def input_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 账号密码登录
    def click_login_password(self):
        self.find_element(*self.login_password_loc).click()

    # 点击选择用验证码登录
    def click_verify_login(self):
        self.find_element(*self.verify_login_loc).click()

    # 输入手机号码
    def input_phone_number(self, phone_number):
        self.find_element(*self.phone_number_loc).clear()
        self.find_element(*self.phone_number_loc).send_keys(phone_number)

    # 点击获取手机验证码
    def click_get_verify_code(self):
        self.find_element(*self.get_verify_code_loc).click()

    # 输入手机验证
    def phone_verify_code(self, phone_verify_code):
        self.find_element(*self.input_verify_code_loc).clear()
        self.find_element(*self.input_verify_code_loc).send_keys(phone_verify_code)

    # 手机验证码登录
    def click_login_verify(self):
        self.find_element(*self.login_verify_loc).click()

    # 获取输入错误时候的提示
    def get_input_error(self):
        return self.find_element(*self.alert_error_loc).text


    '''公用的方法'''
    # 账号密码登录完整步骤
    def user_password_login(self, username, password):
        '''用户名密码登录'''
        self.open()
        sleep(2)
        self.click_password_login()
        self.input_account_number(username)
        self.input_password(password)
        self.click_login_password()
        sleep(1)
