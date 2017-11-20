# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from basePage import PageBase

class XuanZeShuJuPage(PageBase):
    '''选择数据项测试'''

    # 获取选择数据项页面文本
    xuan_ze_shu_ju_page_loc = (By.XPATH, "html/body/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[1]")
    def get_xuan_ze_shu_ju_text(self):
        self.find_element(*self.xuan_ze_shu_ju_page_loc).text()