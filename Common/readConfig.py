# coding:utf-8
__author__ = 'annie'

import os
import codecs # 转编码用
import configparser # 读取配置文件模块

# 获取上层目录
parDir = os.path.dirname(proDir)
# print(parDir)
configPath = os.path.join(parDir,'config.ini')
# print('prodir:',proDir,configPath)

class ReadConfig(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)
        # self.cf.read(configPath,encoding="utf-8-sig")
    def get_email(self,name):
        value = self.cf.get('EMAIL',name)
        return value
    def get_http(self,name):
        value = self.cf.get('HTTP',name)
        return value