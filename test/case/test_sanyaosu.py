# -*- coding:utf-8 -*-
import unittest, sys
from ..page.loginPage import LoginPage
from ..page.sanyaosuPage import SanYaoSuPage
from selenium import webdriver
sys.path.append("../utils")
from utils.config import DATA_PATH, Config
from utils.yaml_reader import ExcelReader
from utils.log import logger
from utils import screenshot
import time


class sanyaosuTest(unittest.TestCase):
    '''三要素验证和进入人工审核测试【需要保证没有正在人工审核中的订单存在】'''
    dr = webdriver.Firefox()
    url = Config().getconf('Login_URL')
    login_page = LoginPage(dr, url, u'登录-知了背调')
    data_login_file = DATA_PATH + '/' + Config().getconf('Login_Test_Data')
    test_login_datas = ExcelReader(data_login_file, title_line=False).data
    login_page.user_password_login(str(int(test_login_datas[4][0])), test_login_datas[4][1])
    def setUp(self, driver=dr):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.url = Config().getconf('Login_URL')
        self.data_sanyaosu_file = DATA_PATH + '/' + Config().getconf('SanYaoSu_Test_Data')
        self.test_sanyaosu_datas = ExcelReader(self.data_sanyaosu_file, title_line=False).data
    def test_SanYaoSu_1(self):
        '''点击开始背调,判断打开的页面是否正确'''
        yaosupage = SanYaoSuPage(self.driver, self.url, u'登录-知了背调')
        yaosupage.click_kai_shi_bei_diao()
        time.sleep(1)
        try:
            self.assertEqual(yaosupage.get_tian_san_yao_su_text(), "填写信息")
            logger.debug(yaosupage.get_tian_san_yao_su_text())
        except:
            screenshot.Cut_img(self.driver, "test_SanYaoSu_1")
            logger.error("与预期信息不匹配")

    def test_SanYaoSu_2(self):
        '''两要素不一致'''
        yaosupage = SanYaoSuPage(self.driver, self.url, u'登录-知了背调')
        yaosupage.input_bei_diao_xing_ming(unicode(self.test_sanyaosu_datas[0][0]))
        yaosupage.input_id_number(str(int(self.test_sanyaosu_datas[0][1])))
        yaosupage.input_phone_number(str(int(self.test_sanyaosu_datas[0][2])))
        yaosupage.input_department(unicode(self.test_sanyaosu_datas[0][3]))
        yaosupage.input_job(unicode(self.test_sanyaosu_datas[0][4]))
        time.sleep(2)
        yaosupage.click_start_button()
        time.sleep(2)
        try:
            self.assertEqual(yaosupage.get_liang_yao_so_text(), "身份证号和姓名不匹配，请确认输入是否有误。")
        except:
            screenshot.Cut_img(self.driver,"test_SanYaoSu_2")
            logger.error("两要素弹框不正确")
        logger.debug(yaosupage.get_liang_yao_so_text())
    def test_SanYaoSu_3(self):
        '''姓名和身份证匹配，手机号不匹配'''
        yaosupage = SanYaoSuPage(self.driver, self.url, u'登录-知了背调')
        yaosupage.input_bei_diao_xing_ming(unicode(self.test_sanyaosu_datas[1][0]))
        yaosupage.input_id_number(str(int(self.test_sanyaosu_datas[1][1])))
        yaosupage.input_phone_number(str(int(self.test_sanyaosu_datas[1][2])))
        yaosupage.click_start_button()
        time.sleep(2)
        try:
            self.assertIn("该手机号与本人身份不匹配", yaosupage.get_ren_gong_text())
            logger.debug(yaosupage.get_ren_gong_text())
        except:
            screenshot.Cut_img(self.driver, "test_SanYaoSu_3")
            logger.error("没有进入人工审核第一步")
    def test_SanYaoSu_4(self):
        '''取消进入人工审核'''
        yaosupage = SanYaoSuPage(self.driver, self.url, u'登录-知了背调')
        yaosupage.input_bei_diao_xing_ming(unicode(self.test_sanyaosu_datas[1][0]))
        yaosupage.input_id_number(str(int(self.test_sanyaosu_datas[1][1])))
        yaosupage.input_phone_number(str(int(self.test_sanyaosu_datas[1][2])))
        yaosupage.click_start_button()
        time.sleep(2)
        yaosupage.click_ren_gong_cancel()
        try:
            self.assertEqual(yaosupage.get_tian_san_yao_su_text(), "填写信息")
            logger.debug(yaosupage.get_tian_san_yao_su_text())
        except:
            screenshot.Cut_img(self.driver, "test_SanYaoSu_4")
            logger.error("取消进入人工审核后没有进入填写信息页面")
    def test_SanYaoSu_5(self):
        '''确认进入人工审核页面'''
        yaosupage = SanYaoSuPage(self.driver, self.url, u'登录-知了背调')
        yaosupage.input_bei_diao_xing_ming(unicode(self.test_sanyaosu_datas[1][0]))
        yaosupage.input_id_number(str(int(self.test_sanyaosu_datas[1][1])))
        yaosupage.input_phone_number(str(int(self.test_sanyaosu_datas[1][2])))
        yaosupage.click_start_button()
        time.sleep(2)
        yaosupage.click_ren_gong_next()
        try:
            self.assertIn("候选人三项信息匹配不一致，即将为您接入人工审核", yaosupage.get_ren_gong_alert_text())
            logger.debug(yaosupage.get_ren_gong_alert_text())
        except:
            screenshot.Cut_img(self.driver, "test_SanYaoSu_5")
            logger.warning("没有弹出即将进入人工审核的提示")
    def test_SanYaoSu_6(self):
        '''关闭即将进入人工审核的弹框'''
        yaosupage = SanYaoSuPage(self.driver, self.url, u'登录-知了背调')
        yaosupage.input_bei_diao_xing_ming(unicode(self.test_sanyaosu_datas[1][0]))
        yaosupage.input_id_number(str(int(self.test_sanyaosu_datas[1][1])))
        yaosupage.input_phone_number(str(int(self.test_sanyaosu_datas[1][2])))
        yaosupage.click_start_button()
        time.sleep(2)
        yaosupage.click_ren_gong_next()
        yaosupage.click_cancel_ren_gong_alert()
        try:
            self.assertEqual(yaosupage.get_tian_san_yao_su_text(), "填写信息")
            logger.debug(yaosupage.get_tian_san_yao_su_text())
        except:
            screenshot.Cut_img(self.driver, "test_SanYaoSu_6")
            logger.error("与预期信息不匹配")
    def test_SanYaoSu_7(self):
        '''确认即将进入人工审核'''
        yaosupage = SanYaoSuPage(self.driver, self.url, u'登录-知了背调')
        yaosupage.input_bei_diao_xing_ming(unicode(self.test_sanyaosu_datas[1][0]))
        yaosupage.input_id_number(str(int(self.test_sanyaosu_datas[1][1])))
        yaosupage.input_phone_number(str(int(self.test_sanyaosu_datas[1][2])))
        yaosupage.click_start_button()
        time.sleep(2)
        yaosupage.click_ren_gong_next()
        yaosupage.click_next_ren_gong_alert()
        try:
            self.assertEqual(yaosupage.get_ren_gong_zhong_text(), "人工审核中")
            logger.debug(yaosupage.get_ren_gong_zhong_text())
        except:
            screenshot.Cut_img(self.driver, "test_SanYaoSu_7")
            logger.error("并没有进入人工审核")
    def tearDown(self):
        self.driver.refresh()
if __name__=='__main__':
    unittest.main()
    #suite = unittest.TestSuite()
    #suite.addTest(sanyaosuTest("test_SanYaoSu_1"))

    #runner = unittest.TextTestRunner()
    #runner.run(suite)