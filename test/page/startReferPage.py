# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase


class StartReferPage(PageBase):
    input_name_loc = (By.ID, "xm")
    input_id_number_loc = (By.ID, "sfz")
    input_phone_number_loc = (By.ID, "sjh")
    input_department_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/label[1]/input")
    input_job_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[1]/label[2]/input")
    start_button_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]")
    qie_pi_liang_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[3]/a")
    xuan_ze_wen_jian_loc = (By.ID, "fileToUpload")
    dao_ru_loc = (By.XPATH, ".//*[@id='uploadform']/div/input[2]")
    xia_zai_mo_ban_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/a")
    pi_liang_start_button_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/button")
    qie_dan_ci_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div/div/a")
    ji_su_miao_cha_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[1]")
    xian_xia_bei_diao_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]")
    S0001_IdentityCheck_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[4]/input")
    S0003_ReturnPhoto_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[4]/div[4]/input")
    S0011_Education_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[6]/div[4]/input")
    S0031_EduVerify_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[7]/div[4]/input")
    S0012_ProfessionCert_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[8]/div[4]/input")
    S0028_ShPersonResume_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[11]/div[1]/input")
    S0035_GzSocialsecurity_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[11]/div[2]/input")
    S0038_SzSocialsecurity_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[11]/div[3]/input")
    S0023_QueryWageGrade_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[11]/div[4]/input")
    S0034_HzSocialsecurity_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[11]/div[5]/input")
    S0037_NjSocialsecurity_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[11]/div[6]/input")
    S0014_PersonalBusinessReg_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[13]/div[4]/input")
    S0020_BlackListCheck_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[15]/div[4]/input")
    S0019_BadInfo_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[16]/div[4]/input")
    S0024_LawCond_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[17]/div[4]/input")
    S0025_LawCond_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[18]/div[4]/input")
    hu_zhao_he_cha_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[3]/div[4]/div/div/input")
    hu_zhao_jian_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[3]/div[4]/div/span[1]")
    hu_zhao_jia_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[3]/div[4]/div/span[2]")
    xue_li_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[5]/div[4]/div/div/input")
    xue_li_jian_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[5]/div[4]/div/span[1]")
    xue_li_jia_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[5]/div[4]/div/span[2]")
    xue_wei_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[6]/div[4]/div/div/input")
    xue_wei_jian_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[6]/div[4]/div/span[1]")
    xue_wei_jia_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[6]/div[4]/div/span[2]")
    jin_rong_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[8]/div[4]/div/div/input")
    jin_rong_jian_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[8]/div[4]/div/span[1]")
    jin_rong_jia_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[8]/div[4]/div/span[2]")
    lv_li_ji_chu_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[10]/div[4]/div/div/input")
    lv_li_ji_jian_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[10]/div[4]/div/span[1]")
    lv_li_ji_jia_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[10]/div[4]/div/span[2]")
    lv_li_sheng_du_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[11]/div[4]/div/div/input")
    lv_li_shen_jian_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[11]/div[4]/div/span[1]")
    lv_li_shen_jia_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[11]/div[4]/div/span[2]")
    biao_xian_ji_chu_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[13]/div[4]/div/div/input")
    biao_xian_ji_jian_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[13]/div[4]/div/span[1]")
    biao_xian_ji_jia_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[13]/div[4]/div/span[2]")
    biao_xian_shen_du_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[14]/div[4]/div/div/input")
    biao_xian_shen_jian_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[14]/div[4]/div/span[1]")
    biao_xian_shen_jia_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div[14]/div[4]/div/span[2]")
    fan_hui_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[4]/div[1]")
    ti_jiao_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[2]/div[4]/div[2]")
    zhi_fu_fan_hui_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[4]/div[1]")
    zhi_fu_ti_jiao_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[3]/div/div/div[4]/div[2]/div[2]")

    # 输入被调人姓名
    def input_name(self, name):
        self.find_element(*self.input_name_loc).clear()
        self.find_element(*self.input_name_loc).send_keys(name)

    # 输入被调人省份证号码
    def input_id_number(self, id_number):
        self.find_element(*self.input_id_number_loc).clear()
        self.find_element(*self.input_id_number_loc).send_keys(id_number)

    # 输入被调人手机号
    def input_phone_number(self, phone_number):
        self.find_element(*self.input_phone_number_loc).clear()
        self.find_element(*self.input_phone_number_loc).send_keys(phone_number)

    # 输入背调人部门
    def input_department(self, department):
        self.find_element(*self.input_department_loc).click()
        self.find_element(*self.input_department_loc).send_keys(department)

    # 输入背调人职位
    def input_job(self, job):
        self.find_element(*self.input_job_loc).click()
        self.find_element(*self.input_job_loc).send_keys(job)

    # 点击开始发起背调
    def click_start_button(self):
        self.find_element(*self.start_button_loc).click()

    # 点击切换为批量背调
    def click_qie_pi_liang(self):
        self.find_element(*self.qie_pi_liang_loc).click()

    # 点击选择文件
    def click_xuan_ze_wen_jian(self):
        self.find_element(*self.xuan_ze_wen_jian_loc).click()

    # 点击下载模板
    def click_xia_zai(self):
        self.find_element(*self.xia_zai_mo_ban_loc).click()

    # 点击开始批量背调
    def click_start_pi_liang(self):
        self.find_element(*self.pi_liang_start_button_loc).click()

    # 点击切换为单次背调
    def click_qie_dan_ci(self):
        self.find_element(*self.qie_dan_ci_loc).click()

    # 点击选择极速秒查
    def click_ji_su_miao_cha(self):
        self.find_element(*self.ji_su_miao_cha_loc).click()

    # 点击线下背调
    def click_xian_xia_bei_diao(self):
        self.find_element(*self.xian_xia_bei_diao_loc).click()

    # 点击选择身份信息简单版
    def click_s001(self):
        self.find_element(*self.S0001_IdentityCheck_loc).click()

    # 点击选择身份信息基础版A
    def click_s003(self):
        self.find_element(*self.S0003_ReturnPhoto_loc).click()

    # 点击选择高等教育
    def click_s0011(self):
        self.find_element(*self.S0011_Education_loc).click()

    # 点击选择技工教育
    def click_s0031(self):
        self.find_element(*self.S0031_EduVerify_loc).click()

    # 点击选择职业资格信息
    def click_s0012(self):
        self.find_element(*self.S0012_ProfessionCert_loc).click()

    # 点击选择上海工作经历
    def click_s0028(self):
        self.find_element(*self.S0028_ShPersonResume_loc).click()

    # 点击选择广州工作经历
    def click_s0035(self):
        self.find_element(*self.S0035_GzSocialsecurity_loc).click()

    # 点击选择深圳工作经历
    def click_s0038(self):
        self.find_element(*self.S0038_SzSocialsecurity_loc).click()

    # 点击选择福建工作经历
    def click_s0023(self):
        self.find_element(*self.S0023_QueryWageGrade_loc).click()

    # 点击选择杭州工作经历
    def click_s0034(self):
        self.find_element(*self.S0034_HzSocialsecurity_loc).click()

    # 点击选择南京工作经历
    def click_s0037(self):
        self.find_element(*self.S0037_NjSocialsecurity_loc).click()

    # 点击选择个人工商信息
    def click_s0014(self):
        self.find_element(*self.S0014_PersonalBusinessReg_loc).click()

    # 点击选择网络黑名单
    def click_s0020(self):
        self.find_element(*self.S0020_BlackListCheck_loc).click()

    # 点击选择违法犯罪信息
    def click_s0019(self):
        self.find_element(*self.S0019_BadInfo_loc).click()

    # 点击选择法院涉法涉诉
    def click_s0024(self):
        self.find_element(*self.S0024_LawCond_loc).click()

    # 点击选择法院失信
    def click_s0025(self):
        self.find_element(*self.S0025_LawCond_loc).click()

    # 输入护照核查
    def input_hu_zhao(self, hu_zhao):
        self.find_element(*self.hu_zhao_he_cha_loc).send_keys(hu_zhao)

    # 点击减少护照份数
    def click_hu_zhao_jian(self):
        self.find_element(*self.hu_zhao_jian_loc).click()

    # 点击增加护照份数
    def click_hu_zhao_jia(self):
        self.find_element(*self.hu_zhao_jia_loc).click()

    # 输入学历份数
    def input_xue_li(self, xue_li):
        self.find_element(*self.xue_li_loc).send_keys(xue_li)

    # 点击减少学历份数
    def click_xue_li_jian(self):
        self.find_element(*self.xue_li_jian_loc).click()

    # 点击增加学历份数
    def click_xue_li_jia(self):
        self.find_element(*self.xue_li_jia_loc).click()

    # 点击输入学位份数
    def input_xue_wei(self, xue_wei):
        self.find_element(*self.xue_wei_loc).send_keys(xue_wei)

    # 点击减少学位份数
    def click_xue_wei_jian(self):
        self.find_element(*self.xue_wei_jian_loc).click()

    # 点击增加学位份数
    def click_xue_wei_jia(self):
        self.find_element(*self.xue_wei_jia_loc).click()

    # 点击输入金融违规
    def input_jin_rong(self, jin_rong):
        self.find_element(*self.jin_rong_loc).send_keys(jin_rong)

    # 点击减少金融份数
    def click_jin_rong_jian(self,):
        self.find_element(*self.jin_rong_jian_loc).click()

    # 点击增加金融份数
    def click_jin_rong_jia(self):
        self.find_element(*self.jin_rong_jia_loc).click()

    # 点击输入工作履历基础班
    def input_lv_li_ji_chu(self, lv_li):
        self.find_element(*self.lv_li_ji_chu_loc).send_keys(lv_li)

    # 点击减少履历基础版
    def click_lv_li_ji_jian(self):
        self.find_element(*self.lv_li_ji_jian_loc).click()

    # 点击增加履历基础版
    def click_lv_li_ji_jia(self):
        self.find_element(*self.lv_li_ji_jia_loc).click()

    # 点击输入履历深度版
    def input_lv_li_shen_du(self, lv_li_shen):
        self.find_element(*self.lv_li_sheng_du_loc).click(lv_li_shen)

    # 点击减少履历深度版
    def click_lv_li_shen_jian(self):
        self.find_element(*self.lv_li_shen_jian_loc).click()

    # 点击增加履历深度版
    def click_lv_li_shen_jia(self):
        self.find_element(*self.lv_li_shen_jia_loc).click()

    # 点击输入表现基础版
    def input_biao_xian_ji_chu(self, biao_xian_ji_chu):
        self.find_element(*self.biao_xian_ji_chu_loc).send_keys(biao_xian_ji_chu)

    # 点击减少表现基础版
    def click_biao_xian_ji_jian(self):
        self.find_element(*self.biao_xian_ji_jian_loc).click()

    # 点击增加表现基础版
    def click_biao_xian_ji_jia(self):
        self.find_element(*self.biao_xian_ji_jia_loc).click()

    # 点击输入表现深度版
    def input_biao_xian_shen_du(self, biao_xian_shen):
        self.find_element(*self.biao_xian_shen_du_loc).send_keys(biao_xian_shen)

    # 点击减少表现深度版
    def click_biao_xian_shen_jian(self):
        self.find_element(*self.biao_xian_shen_jian_loc).click()

    # 点击增加表现深度版
    def click_biao_xian_sheng_jia(self):
        self.find_element(*self.biao_xian_shen_jia_loc).click()

    # 选择数据项页面，点击返回
    def click_fan_hui(self):
        self.find_element(*self.fan_hui_loc).click()

    # 点击提交，进入支付页面
    def click_ti_jiao(self):
        self.find_element(*self.ti_jiao_loc).click()

    # 支付页面点击返回
    def click_zhi_fu_fan_hui(self):
        self.find_element(*self.zhi_fu_fan_hui_loc).click()

    # 点击支付页面确认提交
    def click_zhi_fu_ti_jiao(self):
        self.find_element(*self.zhi_fu_ti_jiao_loc).click()
