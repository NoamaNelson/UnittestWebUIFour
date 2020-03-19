#coding=utf-8
from email.mime.text import MIMEText
import time
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
import email
import os
def sendmain(file_path,mail_to = 'nova_pangjl@126.com'):
    mail_from='nova_jiqun@126.com'
    f = open(file_path,'rb')
    mail_body=f.read()
    f.close()
    
    msg = email.MIMEMultipart.MIMEMultipart() 

    # 构造MIMEBase对象做为文件附件内容并附加到根容器  
    contype = 'application/octet-stream'  
    maintype, subtype = contype.split('/', 1)  
    ## 读入文件内容并格式化  
    data = open(file_path, 'rb')  
    file_msg = email.MIMEBase.MIMEBase(maintype, subtype)  
    file_msg.set_payload(data.read( ))  
    data.close( )  
    email.Encoders.encode_base64(file_msg)  
    ## 设置附件头  
    basename = os.path.basename(file_path)  
    file_msg.add_header('Content-Disposition',  
                        'attachment', filename = basename)  
    msg.attach(file_msg)  
    print u'msg 附件添加成功'
    
    msg1 = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(msg1)
    
    if isinstance(mail_to,str):
        msg['To'] = mail_to
    else: 
        msg['To'] = ','.join(mail_to)
    msg['From'] = mail_from
    msg['Subject']= u'H9Web自动化测试报告'
    msg['date']=time.strftime('%Y-%m-%d-%H_%M_%S')
    print(msg['date'])
  
    
    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('nova_jiqun@126.com','abc123456')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'email has send out !'
if __name__=='__main__':
    sendmain('../report/2017-08-18-10_18_57_result.html')

    
