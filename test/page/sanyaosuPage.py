# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase


class SanYaoSuPage(PageBase):

    '''三要素验证和进入人工审核'''

    # 点击开始背调，进入填写三要素页面
    start_reference_check_loc = (By.CLASS_NAME, "startbd")
    def click_kai_shi_bei_diao(self):
        self.find_element(*self.start_reference_check_loc).click()

    # 获取点击开始背调之后打开的页面的文本
    tian_xie_san_yao_su_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]")
    def get_tian_san_yao_su_text(self):
        return self.find_element(*self.tian_xie_san_yao_su_loc).text

    # 输入背调人姓名
    input_name_loc = (By.ID, "xm")
    def input_bei_diao_xing_ming(self, name):
        self.find_element(*self.input_name_loc).clear()
        self.find_element(*self.input_name_loc).send_keys(name)

    # 输入背调人身份证
    input_id_number_loc = (By.ID, "sfz")
    def input_id_number(self, id_number):
        self.find_element(*self.input_id_number_loc).clear()
        self.find_element(*self.input_id_number_loc).send_keys(id_number)

    # 输入背调人手机号
    input_phone_number_loc = (By.ID, "sjh")
    def input_phone_number(self, phone_number):
        self.find_element(*self.input_phone_number_loc).clear()
        self.find_element(*self.input_phone_number_loc).send_keys(phone_number)

    # 两要素不一致弹框提示文本
    get_laing_yao_su_loc = (By.XPATH, "html/body/div[8]/div/p")
    def get_liang_yao_so_text(self):
        return self.find_element(*self.get_laing_yao_su_loc).text

    # 关闭三要素输入错误提示
    close_input_error_text_loc = (By.XPATH, "html/body/div[8]/div/div")
    def click_close_input_error(self):
        self.find_element(*self.close_input_error_text_loc).click()

    # 输入背调人部门
    input_department_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/label[1]/input")
    def input_department(self, department):
        self.find_element(*self.input_department_loc).clear()
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
    get_san_yao_su_error_text_loc = "html/body/div[7]/div/p"
    def get_san_yao_su_error_text(self):
        return self.find_element(*self.get_san_yao_su_error_text_loc).text

    # 两要素一致，三要素不一致，页面提示文本
    get_ren_gong_text_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/p")
    def get_ren_gong_text(self):
        return self.find_element(*self.get_ren_gong_text_loc).text

    # 人工审核点击下一步
    ren_gong_next_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/button[1]")
    def click_ren_gong_next(self):
        self.find_element(*self.ren_gong_next_loc).click()

    # 取消进入人工审核
    ren_gong_cancel_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/button[2]")
    def click_ren_gong_cancel(self):
        self.find_element(*self.ren_gong_cancel_loc).click()

    # 人工审核弹框标题
    ren_gong_alert_title_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[4]/div/div[2]/p")
    def get_ren_gong_alert_text(self):
        return self.find_element(*self.ren_gong_alert_title_loc).text

    # 人工审核弹框取消
    cancel_ren_gong_alert_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[4]/div/div[3]/span/button[1]")
    def click_cancel_ren_gong_alert(self):
        self.find_element(*self.cancel_ren_gong_alert_loc).click()

    # 人工审核弹框确认
    next_ren_gong_alert_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[4]/div/div[3]/span/button[2]")
    def click_next_ren_gong_alert(self):
        self.find_element(*self.next_ren_gong_alert_loc).click()

    # 开始背调页面，人工审核标记
    ren_gong_shen_he_zhong_loc = (By.XPATH,"html/body/div[2]/div[2]/div[1]/div/div/div[2]/ul/li/div[1]/h4")
    def get_ren_gong_zhong_text(self):
       return self.find_element(*self.ren_gong_shen_he_zhong_loc).text

    # 获取发起背调第二步选择数据项页面文本
    get_xuan_ze_shu_ju_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[1]")
    def get_xuan_sux_text(self):
        return self.find_element(*self.get_xuan_ze_shu_ju_loc).text