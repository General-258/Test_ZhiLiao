# -*- coding:utf-8 -*-
import os
from utils.file_reader import YamlReader

#获取当前文件的绝对路径，其父目录就是该框架的根目录，然后可以通过根目录确定各层的绝对路径
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

class Config:
	'''用于读取配置'''
	def __init__(self, config=CONFIG_FILE):
		self.config = YamlReader(config).data  #读取文件，列表形式返回

	def getconf(self, element, index=0):
		'''
		yaml文件是通过---分节的，用YamlReader读取返回的是一个list，第一项就是默认的节，如果有很多节，用index获取
		这次测试相关的配置全部放在默认节
		'''
		return self.config[index].get(element)