#coding=utf-8

#import unittest,re,sys
from selenium.webdriver.common.action_chains import ActionChains
'''
sys.path.append('..')
sys.path.append('../..')
sys.path.append('../../..')
'''
from com.tools.init_Env import *
from tools.tools import writeConf
import random,json


class Settings(object):
        
    def __init__(self):
        u"""
        ====================================
                    功能：主要是初始化，最大化窗口，以及登录网址获取
        ====================================
        """
        
        init(self)
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get(self.base_url)
        time.sleep(1)
        
    def login(self):
        u"""
        ==============
                    功能：用户登录功能
        ==============
        """
        
        u"登录页面提示信息显示"
        driver=self.driver
        self.login_rompt = driver.find_element_by_class_name(u"login-text").text 
        time.sleep(1)
        login_rompt_welcome = self.login_rompt
        print login_rompt_welcome
        
        u"登录用户名\账号输入"
        account = driver.find_element_by_xpath("html/body/form/div[1]/div/div/input")
        account.clear()
        account.send_keys(self.username)
        time.sleep(0.5)
        
        u"登录密码输入"
        passwd = driver.find_element_by_xpath("html/body/form/div[2]/div/div/input")
        passwd.clear()
        passwd.send_keys(self.password)
        time.sleep(0.5)
        driver.find_element_by_xpath("html/body/form/div[3]/div/button").click()
        time.sleep(1)
        url = driver.current_url
        print url
        return login_rompt_welcome,url
    
    def Custom_Resolution(self):
        u"""
        ======================================================================================
                    功能：在设置界面，设置Test-1的分辨率和刷新率，应用后返回到设备界面查看Test-1的分辨率。并把两处的值进行对比判断，
                                来确定设置的分辨率是否生效或者是否超多带宽     
        ======================================================================================    
        """
       
        i = 1
        myinfo = {}
        
        if i==1:
            u"勾选去掉第一个输入源，选中Test-1输入源"
            time.sleep(0.5)
            self.driver.find_element_by_xpath("html/body/section/header/section[6]").click() #点击设置按钮
            time.sleep(1)
            self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/ul/li[1]/div[1]/label").click() #点击input1-1,目的还取消勾选
            time.sleep(3)
            self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/ul/li[37]/div[1]/label/span[1]/span").click() #点击Test-1，目的是勾选此输入源
        
            u"获取分辨率宽的值"
            time.sleep(2)
            width = self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/div/section[2]/div[2]/div/div[2]/div/div/input")
            width.clear()
            time.sleep(1)
            width.clear()
            width.send_keys("802")
            
            u"获取分辨率高的值"
            height = self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/div/section[3]/div[2]/div/div[2]/div/div/input")
            height.clear()
            time.sleep(1)
            height.clear()
            height.send_keys("602")
            
            u"刷新率值设置和获取"
            time.sleep(1)
            frame_rate1 = self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/div/section[4]/div[2]/div/div/input").get_attribute("value") #获取刷新率的输入框
            self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/div/section[5]/button").click() #点击应用60Hz
            time.sleep(2)
            
            u"获取输入的宽和高"
            width1 = width.get_attribute("value")
            height1 = height.get_attribute("value")
           
            u"在设备界面获取Test-1的分辨率信息"
            self.driver.find_element_by_xpath("html/body/section/header/section[5]").click() #点击设备按钮
            time.sleep(2) 
            self.driver.find_element_by_xpath("html/body/section/section/div/div[1]/div[1]/div[2]/div[11]/div[2]/div[1]/img").click() #点击点击11
            time.sleep(2)
            resolution1 = self.driver.find_element_by_xpath("html/body/section/section/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]").text #获取Test-1的分辨率信息
            #print width1,height1,frame_rate1,resolution1
            
            u"数据存入字典，并把字典转换成列表存入配置文件"
            myinfo = {"width1":width1, "height1":height1, "frame_rate":frame_rate1, "resolution":resolution1}
            time.sleep(1)
            #print myinfo
            writeConf("Resolution", "myinfo1", json.dumps(myinfo))
        
        j = 2
        myinfos = {}
        while(1):
            if j < 3:
                time.sleep(0.5)
                
                self.driver.find_element_by_xpath("html/body/section/header/section[6]").click() #点击设置按钮
                               
                u"获取分辨率宽的值"
                time.sleep(2)
                width2 = self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/div/section[2]/div[2]/div/div[2]/div/div/input")
                width2.clear()
                time.sleep(1)
                width2.clear()
                w1 = random.randint(800,2048)
                width2.send_keys(w1)
            
                u"获取分辨率高的值"
                height2 = self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/div/section[3]/div[2]/div/div[2]/div/div/input")
                height2.clear()
                time.sleep(1)
                height2.clear()
                h1 = random.randint(600,2048)
                height2.send_keys(h1)
            
                u"设置和获取刷新率的值"
                time.sleep(1)
                frame_rate3 = self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/div/section[4]/div[2]/div/div/input").get_attribute("value") #获取刷新率的输入框
                self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/div/section[5]/button").click() #点击应用60Hz
                time.sleep(2)
                
                u"获取输入的宽和高的值"
                width3 = width2.get_attribute("value")
                height3= height2.get_attribute("value")
           
                u"返回到设备界面获取Test-1的分辨率"
                self.driver.find_element_by_xpath("html/body/section/header/section[5]").click() #点击设备按钮
                time.sleep(2) 
                self.driver.find_element_by_xpath("html/body/section/section/div/div[1]/div[1]/div[2]/div[11]/div[2]/div[1]/img").click() #点击点击11
                time.sleep(2)
                resolution3= self.driver.find_element_by_xpath("html/body/section/section/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]").text #获取Test-1的分辨率信息
                #print width2,height2,frame_rate2,resolution2
                
                u"判断带宽是否符合要求"
                if w1!=width3 and h1!=height3:
                    bandwidth = (w1+160)*(h1+62)*60
                    if bandwidth > 165*1000000:
                        print(u"%d超出带宽，无法应用")%bandwidth
                    else:
                        print(u"没有超出带宽，但是设置宽:%d值和高:%d值和显卡返回的不一致")%(w1,h1)
        
                u"把输入值、获取的分辨率值，刷新率写入字典保存"
                myinfos = {"width"+str(j):width3, "height"+str(j):height3, "frame_rate"+str(j):frame_rate3, "resolution"+str(j):resolution3,"W_Input":w1, "H_Input":h1}
                time.sleep(1)
                print myinfos
                
                u"把字典中的信息转换成列表后保存在配置文件中"
                writeConf("Resolution", "myinfo"+str(j), json.dumps(myinfos)) 
                j += 1
            
            else:
                break
      
    def logout(self):
        loginout(self)
        
if __name__=='__main__':
    a = Settings()
    a.login()
    a.Custom_Resolution()

    

    
    
    