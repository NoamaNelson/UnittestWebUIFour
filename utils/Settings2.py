#coding=utf-8

#import unittest,re,sys
from selenium.webdriver.common.action_chains import ActionChains
'''
sys.path.append('..')
sys.path.append('../..')
sys.path.append('../../..')
'''
from com.tools.init_Env import init,loginout
from tools.tools import writeConf
import random,json,time
import xlsxwriter

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
            self.driver.find_element_by_xpath("html/body/section/section/section/main/section/section/ul/li[13]/div[1]/label/span[1]/span").click() #点击Test-1，目的是勾选此输入源
        
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
            self.driver.find_element_by_xpath("html/body/section/section/div/div[1]/div[1]/div[2]/div[6]/div[2]/div[1]/img").click() #点击点击11
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
        workbook = xlsxwriter.Workbook('./rec_data1.xlsx')
        worksheet = workbook.add_worksheet()
        row = 1
        col = 0
        #j = 0
        
        # 设定格式，等号左边格式名称自定义，字典中格式为指定选项
        # bold：加粗，num_format:数字格式
        bold_format = workbook.add_format({'bold': True})
        #money_format = workbook.add_format({'num_format': '$#,##0'})
        #date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
 
        # 将二行二列设置宽度为15(从0开始)
        # worksheet.set_column(1, 1, 15)
 
        # 用符号标记位置，例如：A列1行
        worksheet.write('A1', u'自定义输入的宽', bold_format)
        worksheet.write('B1', u'从自定义框获取的宽', bold_format)
        worksheet.write('C1', u'显卡返回的宽', bold_format)
        
        worksheet.write('D1', u'自定义输入的高', bold_format)
        worksheet.write('E1', u'从自定义框获取的高', bold_format)
        worksheet.write('F1', u'显卡返回的高', bold_format)
        
        worksheet.write('G1', u'自定义获取的刷新率', bold_format)
        worksheet.write('H1', u'显卡返回的刷新率', bold_format)
        
        worksheet.write('I1', u'显卡返回的分辨率', bold_format)
        worksheet.write('J1', u'输入的总带宽', bold_format)
        
        worksheet.write('K1', u'自定义宽输入与自定义获取差值', bold_format)
        worksheet.write('L1', u'自定义宽获取与返回差值', bold_format)
        worksheet.write('M1', u'自定义高输入与自定义获取差值', bold_format)
        worksheet.write('N1', u'自定义高获取与返回差值', bold_format)
        worksheet.write('O1', u'结果', bold_format)
        
        try:
            while(1):
                if j < 202:
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
                    self.driver.find_element_by_xpath("html/body/section/section/div/div[1]/div[1]/div[2]/div[6]/div[2]/div[1]/img").click() #点击点击11
                    time.sleep(2)
                    resolution3= self.driver.find_element_by_xpath("html/body/section/section/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]").text #获取Test-1的分辨率信息
                    #print width2,height2,frame_rate2,resolution2
                
                    u"分割获取到的分辨率"
                    sp = resolution3.split('@')
                    sp1 = sp[0]
                    resolution_split_w = sp1.split('*')[0]
                    resolution_split_h = sp1.split('*')[1]
                    frame_rate3_split = sp[1]
                
                    bandwidth = (w1+160)*(h1+62)*60
                
                    u"判断带宽是否符合要求"
                    if w1!=int(width3) and h1!=int(height3):
                        bandwidth1 = (w1+160)*(h1+62)*60
                        if bandwidth > 165*1000000:
                            print(u"%d超出带宽，无法应用")%bandwidth1
                        else:
                            print(u"输入的值没有生效，请分析！")   
                
                    if resolution_split_w!=int(width3) and resolution_split_h!=int(height3):
                        print(u"没有超出带宽，但是输入的宽:%d和输入的高:%d，与显卡反馈的不一致")%(int(width3),int(height3))            
                
                        u"把输入值、获取的分辨率值，刷新率写入字典保存"
                
                    myinfos = {"W_Input":w1,
                               "width"+str(j):width3,
                               "W_Back":resolution_split_w,
                               "H_Input":h1,
                               "height"+str(j):height3,
                               "H_Back":resolution_split_h,
                               "frame_rate"+str(j):frame_rate3,
                               "Rate_Back":frame_rate3_split,
                               "resolution"+str(j):resolution3,
                               "bandwidth":bandwidth}
            
                    time.sleep(1)
                    print myinfos
                
                    u"把字典中的信息转换成列表后保存在配置文件中"
                    writeConf("Resolution", "myinfo"+str(j), json.dumps(myinfos)) 
                
                    u"使用write_string方法，指定数据格式写入数据到execl表格  "
                    #输入和返回的差值
                    w_difference1 = w1-int(width3)
                    w_difference2 = int(width3)-int(resolution_split_w)
                    h_difference1 = h1-int(height3)
                    h_difference2 = int(height3)-int(resolution_split_h)
                    if w_difference1==0 and w_difference2==0 and h_difference1==0 and h_difference2==0:
                        Result = True
                    else:
                        Result = False
                    worksheet.write_string(row+j, col, str(w1))
                    worksheet.write_string(row+j, col + 1, str(width3))
                    worksheet.write_string(row+j, col + 2, str(resolution_split_w))
                    worksheet.write_string(row+j, col + 3, str(h1))
                    worksheet.write_string(row+j, col + 4, str(height3))
                    worksheet.write_string(row+j, col + 5, str(resolution_split_h))
                    worksheet.write_string(row+j, col + 6, str(frame_rate3))
                    worksheet.write_string(row+j, col + 7, str(frame_rate3_split))
                    worksheet.write_string(row+j, col + 8, str(resolution3))
                    worksheet.write_string(row+j, col + 9, str(bandwidth))
                    worksheet.write_string(row+j, col + 10, str(w_difference1))
                    worksheet.write_string(row+j, col + 11, str(w_difference2))
                    worksheet.write_string(row+j, col + 12, str(h_difference1))
                    worksheet.write_string(row+j, col + 13, str(h_difference2))
                    worksheet.write_string(row+j, col + 14, str(Result))
                    j += 1
                else:
                    break
            workbook.close()
        except Exception as e:
            print(u"出错了，错误信息是：",e)
            workbook.close()
      
    def logout(self):
        loginout(self)
        
if __name__=='__main__':
    a = Settings()
    a.login()
    a.Custom_Resolution()

    

    
    
    