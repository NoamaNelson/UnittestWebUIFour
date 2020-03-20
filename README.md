## 基于Unittest框架，使用Python+Selenium+Webdriver的WebUI自动化测试实例   

## 项目背景
- 测试背景：在业务系统的web页面，有一个分辨率设置功能，而这个功能是自定义的一个区间，用户可以设置分辨率800*600到2048*2048，  
共计1809801个分辨率，如果人工去进行遍历的话，估计得用半年时间，非常费劲
- 解决方案：使用webUI自动化控制分辨率功能的输入，其中每次输入都不重复，遍历所有的分辨率
- 遍历数据解决：如果在脚本中唯一取值，直接由代码生成需要的数据的话，效率非常慢；所以把1809801个分辨率数据直接在txt文本中写入，
只需要打开一次，然后每次从txt取值，直到取完为止
- 业务UI图：  
![](https://i.imgur.com/SPyTh2n.png)  

## 框架环境 
- Python 3.5
- Python的sendmail、xlrd、HTMLtestRuner、CSV、ConfigParser、Json模块
- Selenium
- Pycharm 
## 业务实现思路 
- 设置界面，修改输入源的分辨率的高和宽，以及刷新率，进行应用
- 设备界面，查看对应输入源的分辨率信息
- 把设置界面输入的分辨率信息和设备界面的显卡返回的分辨率信息进行对比，判断设置是否OK

## 业务结果判断
把设置界面输入的分辨率信息和设备界面的显卡返回的分辨率信息进行对比，判断设置是否OK，主要有两种情况： 
- 超出带宽：在脚本中加入判断信息，如果输入的值按照计算公式大于165M带宽，才判断为超出带宽
- 返回异常：输入的和返回的值不一致，这种情况一般保存数据，具体分析，如下示例：  
![](https://i.imgur.com/zGQ7XIA.png)

## 数据处理 
对于运行的结果数据处理，目前支持三种方式：  


- 把测试用例结果，通过HtmlTestRunner.py库封装成测试用例集，然后通过SendMail.py库，发送邮件给项目组成员。
示例：  
![](https://i.imgur.com/FH98i8t.png)

- 使用Eclipse开发平台，把测试结果的Console，保存到log中，实时抓取运行过程和结果数据（这个可以忽略，后续直接在代码中加log）  
![](https://i.imgur.com/9EvMrTa.png)    
- 把测试结果，直接保存到config的配置文件中，直接查看  
![](https://i.imgur.com/gnDIxFC.png)  

## 框架说明
![](https://i.imgur.com/gNmI4DG.png)  
## 操作说明  
1. 打开all_test,py修改接收邮箱地址和保存保存路径
2. 打开tools中的sendMail.py修改发送者的邮箱地址
3. 在Utils中的Settings3写业务模块的功能（Settings1和Settings2是多余的）
4. 在test_case中test_Settings_Custom_Resolution.py写测试用例
5. 执行all_test.py
## 数据存储效果 
![](https://i.imgur.com/fjId7MQ.png)  

