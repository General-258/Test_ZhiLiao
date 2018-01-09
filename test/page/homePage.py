# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase
import time

class HomePage(PageBase):
    '''首页可操作元素定位'''
    # 获取会员类型
    member_type_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section[2]/div/div/div[2]/div/div[1]/h3/span")
    def get_member_type_text(self):
        return self.find_element(*self.member_type_loc).text

    # 获取账户余额
    account_balance_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section[2]/div/div/div[2]/div/div[1]/span[2]")
    def get_account_balance_text(self):
        return self.find_element(*self.account_balance_loc).text

    # 获取所属公司名
    company_name_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section[2]/div/div/div[2]/div/div[1]/h2")
    def get_company_name_text(self):
        return self.find_element(*self.company_name_loc).text

    # 获取登录账户的手机号
    phone_number_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section[2]/div/div/div[2]/div/div[1]/div/div[1]")
    def get_phone_number_text(self):
        return self.find_element(*self.phone_number_loc).text

    # 获取会员有效期
    validity_loc = (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/section[2]/div/div/div[2]/div/div[1]/div/div[2]")
    def get_validity_text(self):
        return self.find_element(*self.validity_loc).text