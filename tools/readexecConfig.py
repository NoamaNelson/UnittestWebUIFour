#coding=utf-8
import xlwt

class CreateEXECFile:
    def __init__(self):

        #创建工作表
        mybook = xlwt.Workbook()
        
        #创建一个sheet，然后在第一行第一列写入内容test
        sheet = mybook.add_sheet(u'sheetname',cell_overwrite_ok=True)#cell_overwrite_ok=True这句话主要是避免重复对单元格操作出错
        sheet.write(0,0,'test')
        sheet.write(0,0,'test1')
        
        #保存新建的excel名称
        mybook.save(u"../xxx.xlsx")
        
        style = xlwt.XFStyle() #初始化样式
        font = xlwt.Font() #为样式创建字体
        font.name = 'Times New Roman'
        font.bold = True
        style.font = font #为样式设置字体
        sheet.write(0, 0, 'some bold Times text', style) # 使用样式
        
        '''
        xlwt 允许单元格或者整行地设置格式。还可以添加链接以及公式。可以阅读源代码，那里有例子：
        dates.py, 展示如何设置不同的数据格式
        hyperlinks.py, 展示如何创建超链接 (hint: you need to use a formula)
        merged.py, 展示如何合并格子
        row_styles.py, 展示如何应用Style到整行格子中.

                     如果你在操作特别大的Excel文件，那么有两个你应该注意的xlrd特性：
        ·open_workbook方法的on_demand参数为True，被访问时会导致只往内存里加载worksheet。
        ·xlrd.Book对象有一个unload_sheet方法能通过指定sheet索引或sheet名称从内存中卸载worksheet。
        '''
       
if __name__== '__main__':
    a = CreateEXECFile()
