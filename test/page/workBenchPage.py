# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase


class WorkBenchPage(PageBase):
    logo_loc = (By.XPATH, "html/body/div[2]/div[1]/div[1]")
    work_bench_loc = (By.XPATH, "html/body/div[2]/div[1]/div[2]")
    yi_shou_quan_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[1]/li[1]")
    dai_shou_quan_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[1]/li[2]")
    yi_ju_jue_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[1]/li[3]")
    yi_qu_xiao_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[1]/li[4]")
    pi_liang_ding_dan_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[2]/li")
    wo_de_tao_can_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[3]/li[1]")
    hui_yuan_zhong_xin_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[3]/li[2]")
    ding_dan_zhong_xin_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[3]/li[3]")
    lian_xi_wo_men_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[4]/li[1]")
    shu_ju_xiang_jie_shao_loc = (By.XPATH, "html/body/div[2]/div[2]/div[2]/ul[4]/li[2]")
    search_butten_loc = (By.CLASS_NAME, "searchBtn")
    search_box_loc = (By.XPATH, "html/body/div[2]/div[1]/div[3]/input")
    tou_xiang_loc = (By.CLASS_NAME, "logout")
    zhang_hao_she_zhi_loc = (By.XPATH, "html/body/div[2]/div[1]/ul[2]/li[2]/div/div/a[1]")
    tuan_dui_cheng_yuan_loc = (By.XPATH, "html/body/div[2]/div[1]/ul[2]/li[2]/div/div/a[2]")
    login_out_loc = (By.XPATH, "html/body/div[2]/div[1]/ul[2]/li[2]/div/div/a[3]")
    see_more_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/a")
    li_ji_shi_yong_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[1]/div[3]/div[2]/div[4]/div[2]/a")

    # 点击logo区域
    def click_logo(self):
        self.find_element(*self.logo_loc).click()

    # 点击工作台
    def click_work_bench(self):
        self.find_element(*self.work_bench_loc).click()

    # 点击已授权
    def click_authorised(self):
        self.find_element(*self.yi_shou_quan_loc).click()

    # 点击待授权
    def click_dai_shou_quan(self):
        self.find_element(*self.dai_shou_quan_loc).click()

    # 点击已拒绝
    def click_yi_ju_jue(self):
        self.find_element(*self.yi_ju_jue_loc).click()

    # 点击已取消
    def click_yi_qu_xiao(self):
        self.find_element(*self.yi_qu_xiao_loc).click()

    # 点击批量订单
    def click_pi_liang(self):
        self.find_element(*self.pi_liang_ding_dan_loc).click()

    # 点击我的套餐
    def click_tao_can(self):
        self.find_element(*self.wo_de_tao_can_loc).click()

    # 点击会员中心
    def click_hui_yuan(self):
        self.find_element(*self.hui_yuan_zhong_xin_loc).cliK()

    # 点击订单中心
    def click_ding_dan(self):
        self.find_element(*self.ding_dan_zhong_xin_loc).click()

    # 点击联系我们
    def click_lian_xi_wo_men(self):
        self.find_element(*self.lian_xi_wo_men_loc).click()

    # 点击数据项介绍
    def click_shu_ju_xiang(self):
        self.find_element(*self.shu_ju_xiang_jie_shao_loc).click()

    # 点击搜索按钮
    def click_search_butten(self):
        self.find_element(*self.search_butten_loc).click()

    # 输入要搜索的内容
    def input_search(self, word):
        self.find_element(*self.search_box_loc).clear()
        self.find_element(*self.search_box_loc).send_keys(word)

    # 点击头像区域
    def click_tou_xiang(self):
        self.find_element(*self.tou_xiang_loc).click()

    # 点击账号设置
    def click_zhang_hao_she_zhi(self):
        self.find_element(*self.zhang_hao_she_zhi_loc).click()

    # 点击团队成员
    def click_tuan_dui_cheng_yuan(self):
        self.find_element(*self.tuan_dui_cheng_yuan_loc).click()

    # 点击退出登录
    def click_login_out(self):
        self.find_element(*self.login_out_loc).click()

    # 点击查看更多
    def click_see_more(self):
        self.find_element(*self.see_more_loc).click()

    # 点击立即使用
    def click_li_ji_shi_yong(self):
        self.find_element(*self.li_ji_shi_yong_loc).click()