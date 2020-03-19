#coding:utf-8
import ConfigParser
import json
import os

def getConf(section,option):
    cp = ConfigParser.ConfigParser()
    if os.path.isfile("./interface.conf"):
        cp.read("./interface.conf")
    elif os.path.isfile("../interface.conf"):
        cp.read("../interface.conf")
    elif os.path.isfile("../../interface.conf"):
        cp.read("../../interface.conf")   
    else:
        raise Exception("wrong path of interface.conf")
    
    return cp.get(section, option)

def store(data):
    u'''
        data: ��Ҫ�������ļ��д洢�����ݣ�һ��ҪΪ�ֵ�����
    '''
    data = dict(load(), **data ) #�������ֵ�ϲ�
    if os.path.isfile("./config.json"):
        with open('./config.json','w') as json_file:
            json_file.write(json.dumps(data))
    elif os.path.isfile("../config.json"):
        with open('../config.json','w') as json_file:
            json_file.write(json.dumps(data))
    elif os.path.isfile('../../config.json'):
        with open('../../config.json','w') as json_file:
            json_file.write(json.dumps(data))
    else:
        raise Exception("wrong path of config.json")  
    
def load():
    if os.path.isfile("./config.json"):
        with open('./config.json') as json_file:
            data = json.load(json_file)
    elif os.path.isfile("../config.json"):
        with open('../config.json') as json_file:
            data = json.load(json_file)
    elif os.path.isfile('../../config.json'):
        with open('../../config.json') as json_file:
            data = json.load(json_file)
    else:
        raise Exception("wrong path of config.json")  
    return data 

if __name__ == "__main__":
    a = getConf("test","old")
    print(a)
    b = {
        "name": "laozhang",
        "old": "28",
        "mm": "oo"
    }
    store(b)