import numpy as np
import pandas as pd
import sys, os, time
import difflib
import hashlib
import datetime
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
from pathlib import Path

#from TextComparison import start_time



path_ExcelOLD = 'xls/DataRecon/'
#path_ExcelNEW = 'xls/NewVersion/'
#PATH3 = 'xls/CompareResults/'
folder1 = os.listdir(path_ExcelOLD) # folder containing your files
#folder2 = os.listdir(path_ExcelNEW) # folder containing your files
#folder3 = os.listdir(PATH3) # folder containing your files
#from flask import Flask
#from flask import request

#app = Flask(__name__)

def excel_diff():
    print("##################### Execution Started #######################")
    start_time = time.time()

    HtmlHeaderStartingString = '<html>' + '\n' + '<head>' + '\n' + '<h1 style = "background-color:powderblue; text-align:center;font-size:30px;">' + '\n' + '<img src = "maveric.png" align = "right" alt = "Italian Trulli" width = "100" height = "35" >EXCEL FILE COMPARISON DASHBOARD</h1>' + '\n' + '<link rel="stylesheet" type="text/css" href="mystyle.css">' + '\n' + '</head>' + '\n' + '<div class="floatLeft" >' + '\n'
    HtmlEndString = '</div>'
    TableStartString = '\n' + '<table align="center"  CELLSPACING=0 CELLPADDING=5 border="1">' + '</br>'
    TableColumnHeaderString = '\n' + '<tr>' + '<th width="30%">' + 'OLDVERSION_VS_NEWVERSION_DIFF_REPORT' + '</th>' + '<th>' + 'OLDVERSION_VS_NEWVERSION FILESIZE' + '</th>' + '<th>' + 'EXECUTION TIME' + '</th>' + '<th>' + 'STATUS' + '</th>' + '<th>' + 'TOTAL DIFFERENCES' + '</th>' + '</tr>' + '</br>'

    #with open("OverallReportExcel.html", 'w') as _file:

        # _file.write(HtmlHeaderStartingString)
        # _file.write(HtmlEndString)
        # _file.write(TableStartString)
        # _file.write(TableColumnHeaderString)

    for item1 in folder1:
        #for item2 in folder2:
           # if (item1 == item2):
               # start_time1 = time.time()
                path_OLD1 = path_ExcelOLD + item1
                # wb = load_workbook(filename='T24SourceFile.xlsx' )
                # wb.save('temp.xlsx')
                # sheet = wb.active
                #
                # values = sheet.values
                # df1 = pd.DataFrame(values)

                #df1.set_index('CURRENCY_CODE', inplace=True)
                #wb.close(filename='temp.xlsx')
                df1 = pd.read_excel('T24SourceFile.xlsx', engine='openpyxl', header=0)
                #df2 = pd.read_excel('OGLBatchFile.xlsx', engine='openpyxl', header=0)
                print(df1.head())
                #print(df2.head())
                #df1.query(str("CURRENCY_CODE") == 'ÁED' and str("ACCOUNTING_DATE") == '20210130')
                #df1 = df1[df1["CURRENCY_CODE"] == 'AED']
                df1 = df1[(df1["CURRENCY_CODE"] == 'AED') & (df1["ACCOUNTING_DATE"] == 20210131) &  (df1["USER_JE_SOURCE_NAME"] == 'T24_UKC')]
                #df2=  df1[df1["ACCOUNTING_DATE"] == '20210130']
                #df1 = df1[df1["ACCOUNTING_DATE"] == '20210130']
               # column = str("CURRENCY_CODE")
                # dump = dump.fillna(0)
                df1 = df1.replace({'nan': 0.0}, regex=True)
                #finaldump = df1["CURRENCY_CODE"]

                finaldump = df1["ACCOUNTED_DR"]
                # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
                total = 0.0
                for eachrow in finaldump:
                   total = float(total) + float(eachrow)
                print('sum: ' + str(total))

                finaldump1 = df1["ACCOUNTED_CR"]
                # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
                total1 = 0.0
                for eachrow in finaldump1:
                 total1 = float(total1) + float(eachrow)
                print('sum: ' + str(total1))





              #  TimeTaken = (end_time1 - start_time1)
def getT24():
                df1 = pd.read_excel('T24SourceFile.xlsx', engine='openpyxl', header=0)
    #df1 = pd.read_excel('T24SourceFile.xlsx', engine='openpyxl', header=0)
                #df2 = pd.read_excel('OGLBatchFile.xlsx', engine='openpyxl', header=0)
                print(df1.head())
                list1 = []
               # print(df2.head())
                #df1.query(str("CURRENCY_CODE") == 'ÁED' and str("ACCOUNTING_DATE") == '20210130')
                #df1 = df1[df1["CURRENCY_CODE"] == 'AED']
                df1 = df1[(df1["CURRENCY_CODE"] == 'AED') & (df1["ACCOUNTING_DATE"] == 20210131) &  (df1["USER_JE_SOURCE_NAME"] == 'T24_UKC')]
                #df2=  df1[df1["ACCOUNTING_DATE"] == '20210130']
                #df1 = df1[df1["ACCOUNTING_DATE"] == '20210130']
               # column = str("CURRENCY_CODE")
                # dump = dump.fillna(0)
                df1 = df1.replace({'nan': 0.0}, regex=True)
                #finaldump = df1["CURRENCY_CODE"]

                finaldump = df1["ACCOUNTED_DR"]
                # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
                total = 0.0
                for eachrow in finaldump:
                   total = float(total) + float(eachrow)
                print('sum: ' + str(total))

                finaldump1 = df1["ACCOUNTED_CR"]
                # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
                total1 = 0.0
                for eachrow in finaldump1:
                 total1 = float(total1) + float(eachrow)
                print('sum: ' + str(total1))
                list1.append(total)
                list1.append(total1)
                print("Resultant list : " + str(list1))
                return list1




def main():
    #path_OLD = Path('xls/OldVersion/AccountStatement1.xls')
    #path_NEW = Path('xls/NewVersion/AccountStatement1.xls')
    #print("##################### Execution Started #######################")
    start_time = time.time()
    list1 = getT24(20210131)
   # list2 = getOGLT24()
   # compare(list1, list2)
    end_time = time.time()
    TimeTaken = (end_time - start_time)
    print('Time Taken For Execution:' + str(round(TimeTaken, 4)))
    print("################ Execution Completed in " + str(TimeTaken) + " ###############")

    with open("OverallReportExcel.html", 'a') as _file:
            TableEndString = '\n' + '</table>'
            TableEndHtmlString = '\n' + '</html>'
            OverallExecutionTime = '\n' + '<p align="center">' 'Overall Execution Time : ' + str(
                round(TimeTaken, 4)) + ' sec' '</p>' + '\n'
            TimeStampString = '\n' + '<p align="center">' + 'Report Generated TimeStamp : ' + str(
                datetime.datetime.now()) + '</p>' + '\n' + '<br/>'
            _file.write(TableEndString)
            _file.write(TableEndHtmlString)
            _file.write(OverallExecutionTime)
            _file.write(TimeStampString)


if __name__ == '__main__':
    main()