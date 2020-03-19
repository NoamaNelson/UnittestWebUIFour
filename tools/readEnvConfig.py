#coding=utf-8
import csv
import os
class ReadCSVFile:
    def __init__(self,path='../test_args.csv'):
        f = None
        if os.path.isfile(path):
            f = file(os.path.abspath(path))
        elif os.path.isfile('../' + path):
            f = file(os.path.abspath('../' + path))
        else:
            f = file(os.path.abspath('./com/test_args.csv'))
        for li in csv.reader(f):
            if len(li) != 2:
                continue
            self.__dict__[li[0].strip()] = li[1].strip()
        f.close()
if __name__== '__main__':
    a = ReadCSVFile()
    print a.password