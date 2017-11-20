# -*- coding:utf-8 -*-
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH, Config

class Logger(object):
	'''对logging进行简单的封装，使得框架可以很简单的打印日志（输出到控制台和日志文件）'''
	def __init__(self, logger_name='TestZhiLiao'):
		self.logger = logging.getLogger(logger_name)  #获取到log文件
		logging.root.setLevel(logging.NOTSET)         #指定日志的最低输出级别，为NOTSET
		c = Config().getconf('log')                   #通过配置文件获取log配置
		self.log_file_name = c.get('file_name') if c and c.get('file_name') else 'test_zhi_liao.log'  #log文件名称
		self.backup_count = c.get('backup') if c and c.get('backup') else 5  #保留日志数量

		# 日志的输出级别
		self.console_output_level = c.get('console_level') if c and c.get('console_level') else 'WARNING'  #控制台日志级别
		self.file_output_level = c.get('file_level') if c and c.get('file_level') else 'DEBUG'  #日志文件级别

		# 日志输出格式
		pattern = c.get('pattern') if c and c.get('pattern') else '%(asctime)s-%(name)s- [%(levelname)s] -%(message)s   '
		self.formatter = logging.Formatter(pattern)

	def get_logger(self):
		'''
		在logging中添加日志句柄并返回，如果logger中已有句柄，则直接返回;
		此处添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
		两个句柄的日志级别不同，在配置文件中可以设置
		'''
		if not self.logger.handlers:    #避免重复日志
			console_handler = logging.StreamHandler()
			console_handler.setFormatter(self.formatter)
			console_handler.setLevel(self.console_output_level)
			self.logger.addHandler(console_handler)

			# 每天重新创建一个日志文件，最多保留backup_count份
			file_handler = TimedRotatingFileHandler(filename = LOG_PATH +'\\log'+ self.log_file_name,
				                                   when = 'D',
				                                   interval = 1,
				                                   backupCount = self.backup_count,
				                                   delay = True,
				                                   encoding = 'utf-8'
				                                  )
			file_handler.setFormatter(self.formatter)
			file_handler.setLevel(self.file_output_level)
			self.logger.addHandler(file_handler)
			return self.logger
logger = Logger().get_logger()