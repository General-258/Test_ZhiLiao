# -*- coding:utf-8 -*-
"Combine tests for gnosis.xml.objectify package(req 2.3+)"
import unittest, doctest
from test.case import test_login
from utils.config import REPORT_PATH
from utils import HTMLTestRunnerCN
import time, logging
suite = doctest.DocTestSuite()
suite.addTest(unittest.makeSuite(test_login.loginTest))

report_file_name = REPORT_PATH +'\\HTML_Report/'+ time.strftime("%Y%m%d_%H_%M") + '_Report.html'
fp = file(report_file_name, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(
    stream=fp,
    title='知了背调',
    description='测试结果描述'
)
runner.run(suite)