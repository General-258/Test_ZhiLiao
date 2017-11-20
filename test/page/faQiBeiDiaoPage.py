# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase
from loginPage import LoginPage
from time import sleep

class FaQiBeiDiaoPage(PageBase):

    # 点击开始发起背调
    start_reference_check_loc = (By.CLASS_NAME, "startbd")
    def click_start_reference_check(self):
        self.find_element(*self.start_reference_check_loc).click()

    # 获取点击发起背调之后打开的页面的文本
    fa_qi_bei_diao_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]")
    def get_fa_qi_bei_diao_text(self):
        return self.find_element(*self.fa_qi_bei_diao_loc).text

    # 输入背调人姓名
    input_name_loc = (By.ID, "xm")
    def input_name(self, name):
        self.find_element(*self.input_name_loc).clear()
        self.find_element(*self.input_name_loc).send_keys(name)
    # 点击光标定位到姓名输入框
    def click_input_name(self):
        self.find_element(*self.input_name_loc).click()

    # 输入背调人身份证号
    input_id_number_loc = (By.ID, "sfz")
    def input_id_number(self, id_number):
        self.find_element(*self.input_id_number_loc).clear()
        self.find_element(*self.input_id_number_loc).send_keys(id_number)
    # 光标定位到身份证输入框
    def click_input_id_number(self):
        self.find_element(*self.input_id_number_loc).click()

    # 输入背调人手机号
    input_phone_number_loc = (By.ID, "sjh")
    def input_phone_number(self, phone_number):
        self.find_element(*self.input_phone_number_loc).clear()
        self.find_element(*self.input_phone_number_loc).send_keys(phone_number)
    # 光标定位到手机号输入框
    def click_input_phone_number(self):
        self.find_element(*self.input_phone_number_loc).click()

    # 获取三要素输入错误的提示
    get_input_error_text_loc = (By.XPATH, "html/body/div[8]/div/p")
    get_fa_qi_frame_loc = (By.ID, "lim_frame")
    def get_input_error_text(self):
        self.switch_frame(self.get_fa_qi_frame_loc)
        return self.find_element(*self.get_input_error_text_loc).text

    # 输入背调人部门
    input_department_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/label[1]/input")
    def input_department(self, department):
        self.find_element(*self.input_department_loc).click()
        self.find_element(*self.input_department_loc).send_keys(department)

    # 输入背调人职位
    input_job_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/label[2]/input")
    def input_job(self, job):
        self.find_element(*self.input_job_loc).click()
        self.find_element(*self.input_job_loc).send_keys(job)

    # 点击开始背调
    start_button_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]")
    def click_start_button(self):
        self.find_element(*self.start_button_loc).click()

    # 获取三要素验证提示文本
    get_san_yao_su_error_text_loc = "html/body/div[9]/div/p"
    def get_san_yao_su_error_text(self):
        self.switch_frame(self.get_fa_qi_frame_loc)
        return self.find_element(*self.get_san_yao_su_error_text_loc).text

    # 两要素一致，三要素不一致，页面提示文本
    get_ren_gong_text_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/p")
    def get_ren_gong_text(self):
        return self.find_element(*self.get_ren_gong_text_loc).text

    # 人工审核点击下一步
    ren_gong_next_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/button[1]")
    def click_ren_gong_next(self):
        self.find_element(*self.ren_gong_next_loc).click()

    # 获取发起背调第二步选择数据项页面文本
    get_xuan_ze_shu_ju_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[1]")
    def get_xuan_sux_text(self):
        return self.find_element(*self.get_xuan_ze_shu_ju_loc).text

    '''公用的方法'''
    # 账号密码成功登录
    def user_password_success_login(self, username, password):
        login_page = LoginPage(self.driver, self.base_url, u'登录-知了背调')
        login_page.user_password_login(username, password)
        self.click_start_reference_check()
        sleep(2)
