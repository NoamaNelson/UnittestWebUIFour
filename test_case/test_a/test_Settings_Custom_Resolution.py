#coding=utf-8

import unittest
from utils.Settings import Settings
from tools import *

class Test_Configure(unittest.TestCase):
    def setUp(self):
        self.a = Settings()   
        #self.a.login()
        
    def test_login(self):
        login_rompt_now = u"欢迎使用"
        now_url = "http://172.16.12.29/Edit"
        returndata = self.a.login()
        print returndata[0]
        print returndata[1]
        print (u"进入到H9主界面的提示信息为:%s"%(returndata[0]))
        print (u"登录成功后的url为:%s"%(returndata[1]))
        self.assertEqual(login_rompt_now, returndata[0], u"进入H9登录页面失败")    
        self.assertEqual(now_url, returndata[1], u"H9登录失败")    
         
        
    #def test_Custom_Resolution(self):
        """
        now_width = 1919
        now_height = 1079
        now_frame_rate = u"60Hz"
        resolution = u"1920*1080@60Hz"
        """
        returndata1 = self.a.Custom_Resolution()
        print (u"设置的分辨率宽为:%s"%(returndata1[0]))
        print (u"设置的分辨率高为:%s"%(returndata1[1]))
        print (u"设置的自定义刷新率为:%s"%(returndata1[2]))
        print (u"设置后显卡返回的分辨率为:%s"%(returndata1[3]))
        returndata2 = (returndata1[3][0]+returndata1[3][1]+returndata1[3][2]+returndata1[3][3])
        returndata3 = (returndata1[3][5]+returndata1[3][6]+returndata1[3][7]+returndata1[3][8])
        returndata4 = (returndata1[3][10]+returndata1[3][11]+returndata1[3][12]+returndata1[3][13])
        self.assertEqual(returndata1[0], returndata2, u"设置的分辨率宽失败")
        self.assertEqual(returndata1[1], returndata3, u"设置的分辨率高失败")
        self.assertEqual(returndata1[2], returndata4, u"设置的自定义刷新率失败")
        
    """
    #def test_basic_information(self):
        print (u"="*40)
        print (u"【首次进入设备界面后，获取到的设备信息如下】：")
        get_listinformation = self.a.Basic_Information() 
        print (u"设备的名称是:%s"%(get_listinformation[0]))
        print (u"设备的MDC地址是:%s"%(get_listinformation[1]))
        print (u"设备的剩余存储空间是:%s"%(get_listinformation[2]))
        print (u"设备的硬件固件版本是:%s"%(get_listinformation[3]))
        print (u"设备的有效屏幕数量是:%s"%(get_listinformation[4]))
        print (u"设备的有效场景数量是:%s"%(get_listinformation[5]))
        print (u"设备的名有效图层数量是:%s"%(get_listinformation[6]))
        print (u"获取设备的基本信息成功")
        print (u"="*40)
        
    #def test_network_settings(self):
        print (u"*"*40)
        print (u"【首次进入到网络设置界面，获取到的网络信息如下】：")
        get_network_settings_now = self.a.Network_Settings() 
        print (u"IP设置方式是:%s"%(get_network_settings_now[0][0]))
        print (u"IP地址是:%s"%(get_network_settings_now[0][1]+get_network_settings_now[0][2]+get_network_settings_now[0][3]+get_network_settings_now[0][4]))
        print (u"子网掩码是:%s"%(get_network_settings_now[0][5]+get_network_settings_now[0][6]+get_network_settings_now[0][7]+get_network_settings_now[0][8]))
        print (u"网关是:%s"%(get_network_settings_now[0][9]+get_network_settings_now[0][10]+get_network_settings_now[0][11]+get_network_settings_now[0][12]))
        print (u"获取网络设置信息成功")
        print (u"*"*40)
        
        print (u"&"*40)
        print (u"【重新修改后的网络信息如下】")
        print (u"IP设置方式是:%s"%(get_network_settings_now[1][0]))
        print (u"IP地址是:%s"%(get_network_settings_now[1][1]+get_network_settings_now[1][2]+get_network_settings_now[1][3]+get_network_settings_now[1][4]))
        print (u"子网掩码是:%s"%(get_network_settings_now[1][5]+get_network_settings_now[1][6]+get_network_settings_now[1][7]+get_network_settings_now[1][8]))
        print (u"网关是:%s"%(get_network_settings_now[1][9]+get_network_settings_now[1][10]+get_network_settings_now[1][11]+get_network_settings_now[1][12]))
        print (u"重新设置网络信息成功")
        print (u"&"*40)
        
        self.a.Synchronization() 
        print (u"@"*40)
        print (u"修改同步模式成功")
        print (u"@"*40)
        
        self.a.Factory_Reset() 
        print (u"$"*40)
        print (u"回复出厂设置成功")
        print (u"$"*40)
        
        self.a.ShutDown() 
        print (u"^"*40)
        print (u"设备已经关机或者重启")
        print (u"^"*40)
        
        self.a.Input() 
        print (u"+"*40)
        print (u"拼接成功")
        print (u"+"*40)
        
        '''
        self.a.Gallery() 
        print (u"-"*40)
        print (u"修改图片名称成功")
        print (u"-"*40)
        '''
        self.a.Output() 
        print (u"#"*40)
        print (u"修改图片名称成功")
        print (u"#"*40)
        
        self.a.Screen() 
        print (u">"*40)
        print (u"屏幕信息修改成功")
        print (u">"*40)
        
    def tearDown(self):
        self.a.logout()
    """
           
if __name__ == "__main__":
    
    '''
    t = unittest.TestSuite()
    t.addTest(Test_Device('test_network_settings')) 
    runner = unittest.TextTestRunner()
    runner.run(t)
    '''
    unittest.main()