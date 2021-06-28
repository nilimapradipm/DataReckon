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

def get_NetBalances1():


    for item1 in folder1:
        #for item2 in folder2:
           # if (item1 == item2):
               # start_time1 = time.time()
                path_OLD1 = path_ExcelOLD + item1

                df1 = pd.read_excel('MXToOGL.xlsx', engine='openpyxl', header=0)

                accounteddr = df1.groupby('SEGMENT3',as_index=False)['ACCOUNTED_DR'].sum()

                accountedcr = df1.groupby('SEGMENT3',as_index=False)['ACCOUNTED_CR'].sum()


                #accounteddr = df1.groupby('GL',as_index=False).agg({'ACCOUNTED_DR': ['sum']})
               # accounteddr = df1.groupby('GL')
                df2 = pd.DataFrame(data=accounteddr)
                df3 = pd.DataFrame(data=accountedcr)
               # merged_Frame = pd.merge(df2, df3, on='SEGMENT3', how='inner',netbalances =('d', lambda merged_Frame:  merged_Frame['ACCOUNTED_DR'] -  merged_Frame['ACCOUNTED_CR']))
                merged_Frame = pd.merge(df2, df3, on='SEGMENT3', how='inner')
                merged_Frame = merged_Frame.assign(NetBalances=lambda merged_Frame: merged_Frame['ACCOUNTED_DR'] -  merged_Frame['ACCOUNTED_CR'])
                #accounteddr.to
                print(df2)
                print(df3)
                print("merged frame")
                print(merged_Frame)

                df1 = pd.read_excel('MUREX_OGL_GCAT.xlsx', engine='openpyxl', header=0)
                m_amount_lcy = df1.groupby('M_GL_CODE', as_index=False)['M_AMOUNT_LCY'].sum()

                df2 = pd.DataFrame(data=m_amount_lcy)

                print(df2)

                df3 = pd.read_excel('MUREX_OGL_CRB.xlsx', engine='openpyxl', header=0)
                m_deallcybal = df3.groupby('M_GL_CODE', as_index=False)['M_DEALLCYBAL'].sum()

                df4 = pd.DataFrame(data=m_deallcybal)

                print(df4)

                df2.rename(columns={"M_GL_CODE": "SEGMENT3"}, inplace=True)
                df4.rename(columns={"M_GL_CODE": "SEGMENT3"}, inplace=True)
                merged_Frame1 = pd.merge(df2, df4, on='SEGMENT3', how='outer')
                print(merged_Frame1)

                df1 = pd.DataFrame({'c1': [1, 4, 7], 'c2': [2, 5, 1], 'c3': [3, 1, 1]})
                df2 = pd.DataFrame({'c4': [1, 4, 7], 'c2': [3, 5, 2], 'c3': [3, 7, 5]})

                print(set(df1.c2).intersection(set(df2.c2)))
                print(set(df2.c2).difference(set(df1.c2)))
                print(set(df1.c2).difference(set(df2.c2)))
                Merged_Frame4 = pd.merge(merged_Frame, merged_Frame1, on='SEGMENT3', how='outer')
                print("----------------Common Keys---------------------")
                print (set(merged_Frame['SEGMENT3']).intersection(set(merged_Frame1['SEGMENT3'])))
                #print(set(merged_Frame['SEGMENT3']).symmetric_difference(set(merged_Frame1['SEGMENT3'])))
                print("----------------Symmetric Differences---------------------")
                print(set(merged_Frame['SEGMENT3']).symmetric_difference(set(merged_Frame1['SEGMENT3'])))
                ##ind = Merged_Frame4.SEGMENT3.isin(merged_Frame.SEGMENT3) & merged_Frame.SEGMENT3.isin(Merged_Frame4.SEGMENT3)
                #print(ind)
                print("----------------")
                print("----------------Common Keys Counts---------------------")
                print(merged_Frame['SEGMENT3'].isin(Merged_Frame4['SEGMENT3']).value_counts())

                print("----------------GL Code which does not exist in main sheet---------------------")
                print(set(Merged_Frame4.SEGMENT3).difference(set(merged_Frame.SEGMENT3)))

                print(Merged_Frame4)
                print(Merged_Frame4.describe())
                print(Merged_Frame4.head())
                Merged_Frame4 = Merged_Frame4.fillna(0)
                Merged_Frame4 = Merged_Frame4.assign(
                Check=lambda Merged_Frame4: Merged_Frame4['NetBalances'] + Merged_Frame4['M_AMOUNT_LCY'] + Merged_Frame4['M_DEALLCYBAL'])
                print(Merged_Frame4)

                Merged_Frame4.to_excel("output.xlsx")

                #type check error to be zero else flag issue
    # accounteddr.to
                #  myd2 = myDict()
               #  myd3 = myDict()
               #  # myd.add(GL,ACCOUNTED_DR )
               #  for inde in df2.index:
               #   print(df2['SEGMENT3'][inde], df2['ACCOUNTED_DR'][inde])
               #   myd2.add(df2['SEGMENT3'][inde], df2['ACCOUNTED_DR'][inde])
               #  print(myd2)
               #
               #  for inde in df3.index:
               #   print(df3['SEGMENT3'][inde], df3['ACCOUNTED_CR'][inde])
               #   myd3.add(df3['SEGMENT3'][inde], df3['ACCOUNTED_CR'][inde])
               #  print(myd3)
               #
               #
               # #netbalances
               #  for inde in df2.index, df3.index:
               #      #if (df2['GL'][inde] == df3['GL'][inde]):
               #      if df2['SEGMENT3'][inde] == df3['SEGMENT3'][inde]:
               #          #net_balances = df2['ACCOUNTED_DR'] - df3['ACCOUNTED_CR']
               #         # df['diff'] = df['market price'] - df['apple price']
               #          print("GL" + df2['SEGMENT3'] + " " + "net_balances")
               #


def get_MXAccountedDR():


    for item1 in folder1:
        #for item2 in folder2:
           # if (item1 == item2):
               # start_time1 = time.time()
                path_OLD1 = path_ExcelOLD + item1

                df1 = pd.read_excel('MXToOGL.xlsx', engine='openpyxl', header=0)

                accounteddr = df1.groupby('SEGMENT3',as_index=False)['ACCOUNTED_DR'].sum()

                #accountedcr = df1.groupby('SEGMENT3',as_index=False)['ACCOUNTED_CR'].sum()

                #accounteddr = df1.groupby('GL',as_index=False).agg({'ACCOUNTED_DR': ['sum']})
               # accounteddr = df1.groupby('GL')
                df2 = pd.DataFrame(data=accounteddr)

                print(df2)

                myd2 = myDict()

                # myd.add(GL,ACCOUNTED_DR )
                for inde in df2.index:
                 print(df2['SEGMENT3'][inde], df2['ACCOUNTED_DR'][inde])
                 myd2.add(df2['SEGMENT3'][inde], df2['ACCOUNTED_DR'][inde])
                print(myd2)
                return myd2

def get_MXAccountedCR():
    for item1 in folder1:
        # for item2 in folder2:
        # if (item1 == item2):
        # start_time1 = time.time()
        path_OLD1 = path_ExcelOLD + item1

        df1 = pd.read_excel('MXToOGL.xlsx', engine='openpyxl', header=0)


        accountedcr = df1.groupby('SEGMENT3', as_index=False)['ACCOUNTED_CR'].sum()

        # accounteddr = df1.groupby('GL',as_index=False).agg({'ACCOUNTED_DR': ['sum']})
        # accounteddr = df1.groupby('GL')
        df3 = pd.DataFrame(data=accountedcr)

        print(df3)

        myd3 = myDict()

        # myd.add(GL,ACCOUNTED_DR )
        for inde in df3.index:
            print(df3['SEGMENT3'][inde], df3['ACCOUNTED_CR'][inde])
            myd3.add(df3['SEGMENT3'][inde], df3['ACCOUNTED_CR'][inde])
        print(myd3)
        return myd3



def get_NetBalances(mydict1, mydict2):
    myd = myDict()
    #myd = myDict()
    for k in mydict1:
        print(mydict1[k])
        print(mydict2[k])
        diff = mydict1[k]-mydict2[k]
        print (diff)


        myd.add(k, diff)
    print("check")
    print(myd)
    return myd


def getMerge():
    df1 = pd.read_excel('MUREX_OGL_GCAT.xlsx', engine='openpyxl', header=0)
    m_amount_lcy = df1.groupby('M_GL_CODE', as_index=False)['M_AMOUNT_LCY'].sum()

    df2 = pd.DataFrame(data=m_amount_lcy)

    print(df2)

    df3 = pd.read_excel('MUREX_OGL_CRB.xlsx', engine='openpyxl', header=0)
    m_deallcybal = df3.groupby('M_GL_CODE', as_index=False)['M_DEALLCYBAL'].sum()

    df4 = pd.DataFrame(data=m_deallcybal)

    print(df4)

    df2.rename(columns={"M_GL_CODE": "SEGMENT3"}, inplace=True)
    df4.rename(columns={"M_GL_CODE": "SEGMENT3"}, inplace=True)
    merged_Frame1 = pd.merge(df2, df4, on='SEGMENT3', how='outer')
    print(merged_Frame1.head())


def getGCATData():
    df1 = pd.read_excel('MUREX_OGL_GCAT.xlsx', engine='openpyxl', header=0)
    m_amount_lcy = df1.groupby('M_GL_CODE', as_index=False)['M_AMOUNT_LCY'].sum()

    df2 = pd.DataFrame(data=m_amount_lcy)

    print(df2)

    df1 = pd.read_excel('MUREX_OGL_CRB.xlsx', engine='openpyxl', header=0)
    m_deallcybal = df1.groupby('M_GL_CODE', as_index=False)['M_DEALLCYBAL'].sum()

    df2 = pd.DataFrame(data=m_deallcybal)

    print(df2)

    # myd = myDict()
    #
    # for index in df2.index:
    #     print(df2['M_GL_CODE'][index], df2['M_AMOUNT_LCY'][index])
    #     myd.add(df2['M_GL_CODE'][index], df2['M_AMOUNT_LCY'][index])
    # print(myd)
    return df2


def getCRBData():
    df1 = pd.read_excel('MUREX_OGL_CRB.xlsx', engine='openpyxl', header=0)
    m_deallcybal = df1.groupby('M_GL_CODE', as_index=False)['M_DEALLCYBAL'].sum()

    df2 = pd.DataFrame(data=m_deallcybal)

    print(df2)
    # myd = myDict()
    #
    # for index in df2.index:
    #     print(df2['M_GL_CODE'][index], df2['M_DEALLCYBAL'][index])
    #     myd.add(df2['M_GL_CODE'][index], df2['M_DEALLCYBAL'][index])
    # print(myd)
    return df2

def Merge(dict1, dict2):
    res = dict1 | dict2
    return res

# def doDataRecon(mydict3,mydict4,mydict5):
#     #mydict6 = myDict()
#     z = mydict4.copy()
#     z.update(mydict5)
#     #mydict6 = Merge(mydict4,mydict5)
#     print(z)
#     #print (mydict3)
#     #print(mydict4)
#     #print(mydict5)
#     k1 =set (mydict3.keys())
#     print(k1)
#     k2 = set(z.keys())
#     print(k2)
#     common_keys = set(k1).intersectionset(k2)
#     myd = myDict()
#     for key in common_keys:
#         #if mydict3[key] == z[key]:
#             print("hi")
#             #print(key + ":" + str(mydict3[key]) + "  " + str(mydict4[key]))
#             diff =  mydict3[key] + z[key]
#         # diff = 0
#             print(diff)
#
#         #myd = myDict()
#             myd.add(key, diff)
#
#     print(myd)
#     return myd



class myDict(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value




def main():
    #path_OLD = Path('xls/OldVersion/AccountStatement1.xls')
    #path_NEW = Path('xls/NewVersion/AccountStatement1.xls')
    #print("##################### Execution Started #######################")
    start_time = time.time()
    get_NetBalances1()
    #getMerge()")
    # print("hello")
    # print(mydict3)
    # mydict4 = getCRBData()
    # mydict5 = getGCATData()

    # verify summation of netbalances + CRB + GCAT is zero
    #mydict6 = doDataRecon(mydict3,mydict4,mydict5)

    # comapre netb
    #finalMerge()
    # mydict1 = get_MXAccountedDR()
    # mydict2 = get_MXAccountedCR()
    # mydict3 = get_NetBalances(mydict1,mydict2)
    # print("helloalance with crb
    # if it starts GL code

    # comapre netbalance with gcat

    # nte change should be netbalnce + net crb + net grb -> 0 or blank
    # from netbalance - gl code if not exist in crb/gcat  put - checks for gl code blank data

    end_time = time.time()
    TimeTaken = (end_time - start_time)
    print('Time Taken For Execution:' + str(round(TimeTaken, 4)))
    print("################ Execution Completed in " + str(TimeTaken) + " ###############")



if __name__ == '__main__':
    main()