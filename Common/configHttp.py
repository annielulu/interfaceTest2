# coding:utf-8
__author__ = 'annie'

import requests
from common import readConfig as readConfig
localReadConfig = readConfig.ReadConfig

class ConfigHttp(object):
    def get(self,url,param,cookie=None,header=None,timeout=3):
        try:
            # print(url,param)
            response = requests.get(url=url,params=eval(param),data=None,header=header,cookies=cookie,timeout=timeout)
            result = response.text
            return result
        except Exception as msg:
            print('request error,please check out!')
            return None
    def post(self,url,param,cookie=None,header=None,timeout=3):
        try:
            response = requests.post(url=url,data=eval(param),param=None,headers=header,cookies=cookie,timeout=timeout)
            result = response.text
            # print(result)
            return result
        except Exception as msg:
            print('request error,please check out!')
            return None
    def getRequest(self,url,method,param):
        if str(method) == 'get':
            return self.get(url,param)
        elif str(method) == 'post':
            return self.post(url,param)