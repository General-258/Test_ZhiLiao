# -*-coding:utf-8 -*-
#from selenium import webdriver
from driver import StartBrowser
import unittest
class ZLTest(unittest.TestCase):
    def setUp(self):
        self.driver = StartBrowser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    unittest.main()
'''
 定义ZLTest()类用于集成unittest.TestCase类，因为笔者创建的所有测试类中setUp()
 与tearDown()方法所做的事情相同，所以，将他们抽象为ZLTest()类，好处就是在编写测
 试用例时不再考虑这两个方法的实现
'''