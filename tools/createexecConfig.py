#coding=utf-8
from xlrd import open_workbook


class ReadEXECFile:
    def __init__(self,path=u'../第26周周报-测试部 - 张博.xlsx'):

        #打开工作表
        book = open_workbook(u'../第26周周报-测试部 - 张博.xlsx')
        print book.nsheets#打印sheet的个数
        
        #获取工作所有sheet的名称
        f =  book.sheet_names()
        print repr(f).decode('unicode_escape')
        
        sheet = book.sheets()[0]
        #sheet = file.sheet_by_index(0)
        #heet = file.sheet_by_name(u'Sheet1')
        
        #获取所有的行和列
        print sheet.nrows
        print sheet.ncols
        
        #循环获取所有的行
        '''
        for rownum in range(sheet.nrows):
            print repr(sheet.row_values(rownum)).decode('unicode_escape')
        '''
        
        #获取某一整行或整列的数据
        '''
        print repr(sheet.row_values(0)).decode('unicode_escape')
        print repr(sheet.col_values(0)).decode('unicode_escape')
        '''
        
        #通过索引获取单元格
        print repr(sheet.cell(0,0).value).decode('unicode_escape')
        print repr(sheet.cell(2,3).value).decode('unicode_escape')

        #通过小标获取单元格
        print repr(sheet.row_values(1)[1]).decode('unicode_escape')
        print repr(sheet.col_values(1)[3]).decode('unicode_escape')
       
if __name__== '__main__':
    a = ReadEXECFile()
