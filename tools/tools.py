#coding=utf-8

import configparser
import os

conf= configparser.ConfigParser()

"""
def readConf():
    '''读取配置文件'''
    #root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf.read("/interface.conf") # 文件路径
    print(conf)
    name = conf.get("mysql", "host")  # 获取指定section 的option值
    print(name)
"""
def writeConf(mysql, host, data):
    '''写入配置文件'''
    #root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf.read('./com/interface.conf')  # 文件路径
 
    conf.set(mysql, host, data)  # 修改指定section 的option
    conf.write(open('./com/interface.conf', 'w'))


"""
[mysql]
host = 1234
port = 3306
user = root
password = Zhsy08241128

import configparser
import os
conf= configparser.ConfigParser()
def readConf():
    '''读取配置文件'''
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf.read(root_path + '/ceshi/conf/app.conf')  # 文件路径
    print(conf)
    name = conf.get("mysql", "host")  # 获取指定section 的option值
    print(name)

def writeConf():
    '''写入配置文件'''
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf.read(root_path + '/ceshi/conf/app.conf')  # 文件路径
 
    conf.set("mysql", "host", "1234")  # 修改指定section 的option
    conf.write(open(root_path + '/ceshi/conf/app.conf', 'w'))
"""



if __name__ == "__main__" :
    myinfos = "{}"
    writeConf("mysql", "host", myinfos)
    