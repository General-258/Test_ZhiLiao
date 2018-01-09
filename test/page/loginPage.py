# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase
import time

class LoginPage(PageBase):
    '''登录页面可操作元素定位'''
    # 打开页面
    def open(self):
        self._open(self.base_url, self.page_title)

    # 输入账户名
    account_number_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/section[2]/div/div/ul/li[1]/div/input")
    def input_accout_loc(self, account_number):
        self.find_element(*self.account_number_loc).clear()
        self.find_element(*self.account_number_loc).send_keys(account_number)

    # 输入登录密码
    password_number_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/section[2]/div/div/ul/li[2]/div/input")
    def input_password_number(self, password_number):
        self.find_element(*self.password_number_loc).clear()
        self.find_element(*self.password_number_loc).send_keys(password_number)

    # 点击登录
    login_button_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/section[2]/div/div/ul/li[4]/button")
    def click_login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 获取弹框的提示文本
    prompt_text_loc = (By.XPATH, "/html/body/div[5]/p")
    def get_prompt_text(self):
        return self.find_element(*self.prompt_text_loc).text

    # 勾选/不勾选忘记密码
    remerber_password_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/section[2]/div/div/ul/li[3]/div/label/span[2]")
    def click_remerber_password(self):
        self.find_element(*self.remerber_password_loc).click()

    # 找回密码链接
    retrieve_password_loc = (By.CLASS_NAME, "forgot")
    def click_retrieve_password(self):
        self.find_element(*self.retrieve_password_loc).click()

    # 登录方法
    def test_login(self, account_number, password):
        self.open()
        time.sleep(2)
        self.input_accout_loc(account_number)
        self.input_password_number(password)
        self.click_login_button()
