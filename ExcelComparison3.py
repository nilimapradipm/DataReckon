import numpy as np
import pandas as pd
import sys, os, time
import difflib
import hashlib
import datetime
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
from pathlib import Path





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
                df2 = pd.read_excel('OGLBatchFile1.xlsx', engine='openpyxl', header=0)
                print(df1.head())
                print(df2.head())

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

                df2.rename(columns={"Journal Name": "Journal_Name"}, inplace=True)
                df2.rename(columns={"Journal Credit": "Journal_Credit"}, inplace=True)
                df2.rename(columns={"Journal Debit": "Journal_Debit"}, inplace=True)

                s = "T24_UKC_20210131 Interface AED"
                df2 = df2[(df2["Journal_Name"] == s)]

                finaldump3 = df2["Journal_Debit"]
                # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
                total2 = 0.0
                for eachrow in finaldump3:
                  total2 = float(total2) + float(eachrow)
                print('sum db: ' + str(total2))

                finaldump4 = df2["Journal_Credit"]
                # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
                total3 = 0.0
                for eachrow in finaldump4:
                 total3 = float(total3) + float(eachrow)
                print('sum cr: ' + str(total3))

    #return total

                # df_OLD = pd.read_excel(path_OLD1).fillna(0)
                #df1 = pd.read_excel(path_OLD1)
                #sheet = wb.get_sheet_by_name ('Sheet1')
               # df = DataFrame(wb.get_sheet_by_name ('Sheet1')values)
                #df1 = pd.read_excel(path_OLD1,engine='openpyxl' )
               # writer = pd.ExcelWriter(path_OLD1 , engine='openpyxl')
        # result.to_excel(writer, sheet_name='DIFF', index=True)
               # df1.to_excel(writer, sheet_name='Sheet1', index=True)
                print(df1.head())
                #for col in df1.columns:
                     #print(list(df1.columns))
        #df1.get(col)
                #for r in dataframe_to_rows(df1, index=True, header=True):
                #df1.rename(columns=df1.iloc[0], inplace=True)
                 # print(list(df1.columns))
                #df1 = df1.set_index('CURRENCY_CODE')
                  #while (df1.iloc[3] == "AED" ):
                   #ch1 =  df1.iloc[4].sum()
                   #rint(ch1)
                print(df1.loc[(df1["CURRENCY_CODE"] == 'AED') & (df1["USER_JE_SOURCE_NAME"] == 'T24_UKC') & (df1["ACCOUNTING_DATE"] == '20210130'), "ACCOUNTED_CR"].sum());
               # print(df1.query("CURRENCY_CODE == AED")['ACCOUNTED_DR'].sum())
               # print(np.where(df1["CURRENCY_CODE"] == 'ÁED', df1["ACCOUNTED_DR"], 0).sum())
        #             #df2.to_excel(writer, sheet_name='NewVersion', index=True)
                #df1.to_excel("xls/CompareResults/b.xls", index=True)
                # print(df_OLD)
                #path_NEW1 = path_ExcelNEW + item2
                # df_NEW = pd.read_excel(path_NEW1).fillna(0)
                #df2 = pd.read_excel(path_NEW1, header=None)

                #df3 = df1.append(pd.Series(['----------------------------- OLD VERSION VS NEW VERSION SEPERATOR -----------------------------']), ignore_index=True)
               # print(df1)

                #result = df3.append(df2)

                # result = result.drop_duplicates(keep=False)
                #
                # print(result)
                # total: int = len(result) - 1
                # number: int = 0
                # # print(Total Differences)
                # # print(number)
                #
                # if (total == 0):
                #     status = 'Matched'
                # else:
                #     status = 'Differences'
                # print(status)


               # result.loc[~result.index.isin(df2.index), 'Status'] = 'new'
               # result.loc[~result.index.isin(df1.index), 'Status'] = 'new'
               #idx = result.stack().groupby(level=[0, 1]).nunique()
               #result.loc[idx.mask(idx <= 1).dropna().index.get_level_values(0), 'Status'] = 'MODIFIED'


               #fname = '{}vs{}.xls'.format(os.path.splitext(item1)[0], os.path.splitext(item2)[0])

               # writer = pd.ExcelWriter("xls/DataRecon/" + fname, engine='xlsxwriter')
                #result.to_excel(writer, sheet_name='DIFF', index=True)
               # df1.to_excel(writer, sheet_name='OldVersion', index=True)
                #df2.to_excel(writer, sheet_name='NewVersion', index=True)

                # get xlsxwriter objects


               # writer.save()

                print('\nDone.\n')


                size1 = os.path.getsize(path_OLD1)
                #size2 = os.path.getsize(path_NEW1)

                end_time1 = time.time()

              #  TimeTaken = (end_time1 - start_time1)

def getT24(currency_code, accounting_date, user_je_source_name):
                df1 = pd.read_excel('T24SourceFile.xlsx', engine='openpyxl', header=0)

                print(df1.head())
                list1 = []
               # print(df2.head())
                #df1.query(str("CURRENCY_CODE") == 'ÁED' and str("ACCOUNTING_DATE") == '20210130')
                #df1 = df1[df1["CURRENCY_CODE"] == 'AED']

                df1 = df1[(df1["CURRENCY_CODE"] == currency_code) & (df1["ACCOUNTING_DATE"] == accounting_date) & (
                            df1["USER_JE_SOURCE_NAME"] == user_je_source_name)]
               # print("------")
               # print(df1)
               # df1 = df1[(df1["CURRENCY_CODE"] == 'AED') & (df1["ACCOUNTING_DATE"] == 20210616) &  (df1["USER_JE_SOURCE_NAME"] == 'T24_UKC')]
                print("POST APPLYING FILTER DATA FROM T24")
                print(df1)

                df1 = df1.replace({'nan': 0.0}, regex=True)


                finaldump = df1["ACCOUNTED_DR"]

                total = 0.0
                for eachrow in finaldump:
                   total = float(total) + float(eachrow)
                print('Data from T24 : ACCOUNTED_DB: ' + str(total))

                finaldump1 = df1["ACCOUNTED_CR"]

                total1 = 0.0
                for eachrow in finaldump1:
                 total1 = float(total1) + float(eachrow)
                print('Data from T24 : ACCOUNTED_CR: ' + str(total1))
                list1.append(total)
                list1.append(total1)
              #  print("Resultant list : " + str(list1))
                return list1

def getOGLT24(journal_name):
    df2 = pd.read_excel('OGLBatchFile.xlsx', engine='openpyxl', header=0)
    df2.rename(columns={"Journal Name": "Journal_Name"}, inplace=True)
    df2.rename(columns={"Journal Credit": "Journal_Credit"}, inplace=True)
    df2.rename(columns={"Journal Debit": "Journal_Debit"}, inplace=True)
    list2 = []
   # s = "T24_UKC_20210131 Interface AED"
    df2 = df2[(df2["Journal_Name"] == journal_name)]
    print("POST APPLYING FILTER DATA FROM OGL")
    print(df2)
    finaldump3 = df2["Journal_Debit"]
    # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
    total2 = 0.0
    for eachrow in finaldump3:
        total2 = float(total2) + float(eachrow)
    print('OGL JOURNAL DEBIT: ' + str(total2))

    finaldump4 = df2["Journal_Credit"]
    # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
    total3 = 0.0
    for eachrow in finaldump4:
        total3 = float(total3) + float(eachrow)
    print('OGL JOURNAL CREDIT: ' + str(total3))
    list2.append(total2)
    list2.append(total3)
    #print("Resultant list : " + str(list2))
    return list2


def compare(list1, list2):
    if (list1[0] == list2[0]) & (list1[1] == list2[1]):
        print("T24 & OGL Data Match")
        return True
    if (list1[0] != list2[0]) & (list1[1] != list2[1]):
        print("T24 & OGL Data MisMatch")
        return False
    if (list1[0] != list2[0]) & (list1[1] == list2[1]):
        print("T24 & OGL Data MisMatch")
        return False
    if (list1[0] == list2[0]) & (list1[1] != list2[1]):
        print("T24 & OGL Data MisMatch")
        return True


def main():

    #print("##################### Execution Started #######################")
    start_time = time.time()
    #T24 DATA
    currency_code = "AED"
    date = 20210616
    user_je_source_name = "T24_UKC"
    category = "Interface"
    #OGL DATA
    journal_name = user_je_source_name + "_" + str(date) + " " + category + " " +currency_code

    #Get T24 Data
    list1 = getT24(currency_code, date, user_je_source_name)
   # list2 = getOGLT24("T24_UKC_20210616 Interface AED")

    # Get OGL Data
    list2 = getOGLT24(journal_name)

    #DATA RECKON
    compare(list1, list2)

    end_time = time.time()
    TimeTaken = (end_time - start_time)
    print('Time Taken For Execution:' + str(round(TimeTaken, 4)))
    print("################ Execution Completed in " + str(TimeTaken) + " ###############")




if __name__ == '__main__':
    main()