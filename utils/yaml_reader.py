# -*- coding:utf-8 -*-
import yaml
import os


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):   #判断该文件是否存在
            self.yamlf = yamlf
        else:
            raise IOError('文件名不存在')
        self._data = None    #定义一个私有变量为none

    @property   # 把方法变成属性调用
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表
        return self._data
