#coding=utf-8
import unittest
import HTMLTestRunner
import time
from tools.sendMail import sendmain
import sched
schedule = sched.scheduler(time.time, time.sleep)
def createHTML():
    test_dir='./test_case'
    discover=unittest.defaultTestLoader.discover(test_dir,
                    pattern='test_*.py',
                    #pattern='test_role.py',
                    top_level_dir=None)
    now=time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
    filename="./report/"+now+'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
                                         stream=fp,
                                         title=u'测试结果',
                                         description=u'全部测试用例')
    #如果想生成HTML数据，就把下面一行注释掉
    #runner=unittest.TextTestRunner()
    runner.run(discover)
    fp.close()
    time.sleep(3)
    sendmain(filename,mail_to=['nova_zhangbo@126.com'])

if __name__=='__main__':
    print("run every day :") 
    createHTML()
