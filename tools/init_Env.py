# -*- coding: utf-8 -*-
from selenium import webdriver
from com.tools.readEnvConfig import ReadCSVFile
import time

def init(self):
    config = ReadCSVFile()
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30)
    self.accept_next_alert = True
    self.base_url = config.base_url
    self.username = config.username
    self.password = config.password
    self.email_addrs = config.email_addrs
    #self.login_rompt = config.login_rompt
    
def loginout(self):
    time.sleep(1)
    self.driver.quit()
