# -*- coding:utf-8 -*-
from xml.dom import minidom
from config import DATA_PATH


class GetXMLTestData(object):
    '''xmlname--文件名； nodename--节点名，也就是标签名； nodeid--索引值，节点的索引值； nodeattribute--节点的属性'''
    # 获取节点属性
    def getxmlattribute(self, xmlname, nodename, indexid, nodeattribute):
        root = minidom.parse(xmlname)
        return root.documentElement.getElementsByTagName(nodename)[indexid].getAttribute(nodeattribute)

    # 获取节点名
    def getxmlnodeValue(self, xmlname, nodename, indexid):
        root = minidom.parse(xmlname)
        return root.documentElement.getElementsByTagName(nodename)[indexid].childNodes[0].nodeValue

    # 获取node个数
    def getxmlnodenum(self, xmlname, nodename):
        root = minidom.parse(xmlname)
        return len(root.documentElement.getElementsByTagName(nodename))

    # 获取xml的路径
    @property
    def getTestDataPath_xml(self):
        testdatapath = DATA_PATH
        return testdatapath