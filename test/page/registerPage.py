# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase


class RegisterPage(PageBase):
    company_email_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/input")
    company_phone_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/input")
    gain_verify_loc = (By.ID, "hqyzm")
    photo_verify_loc = (By.CSS_SELECTOR, "input.el-input__inner")
    submit_photo_verify_loc = (By.CSS_SELECTOR, "button.el-button.el-button--primary")
    phone_verify_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div/input")
    one_next_step_loc = (By.XPATH, "html/body/div[2]/div[2]/div/div/div[2]/form/div[4]/div/button")

    # 打开页面
    def open(self):
        self._open(self.base_url, self.page_title)

    # 输入企业邮箱
    def input_company_email(self, company_email):
        self.find_element(*self.company_email_loc).send_keys(company_email)

    # 输入企业电话号码
    def input_company_phone(self, company_phone):
        self.find_element(*self.company_phone_loc).send_keys(company_phone)

    # 点击获取手机验证码
    def click_gain_verify(self):
        self.find_element(*self.gain_verify_loc).click()

    # 点击发送验证码之后，打开图形验证码输入弹框,输入图形验证码
    def input_photo_verify(self, photo_verify):
        self.find_element(*self.photo_verify_loc).clear()
        self.find_element(*self.photo_verify_loc).send_keys(photo_verify)

    # 点击提交图形验证码进行验证
    def click_submit_photo_verify(self):
        self.find_element(*self.submit_photo_verify_loc).click()

    # 输入手机验证码
    def input_phone_verify(self, phone_verify):
        self.find_element(*self.phone_verify_loc).send_keys(phone_verify)

    # 第一步点击下一步
    def click_one_next_step(self):
        self.find_element(*self.one_next_step_loc).click()
