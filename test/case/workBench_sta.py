# -*- coding:utf-8 -*-
from time import sleep
import unittest, sys
sys.path.append("./Model")
sys.path.append("./PageObject")
from Model import screenshot
from PageObject.loginPage import LoginPage
from selenium import webdriver


class workBenchTest(unittest.TestCase):
    '''工作台页面功能'''
    def setUp(self):
        pass