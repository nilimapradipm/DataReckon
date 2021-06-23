import numpy as np
import pandas as pd
import sys, os, time
import difflib
import hashlib
import datetime

from datetime import datetime
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
from pathlib import Path

#from TextComparison import start_time
from typing import re

path_ExcelOLD = 'xls/DataRecon/'
#path_ExcelNEW = 'xls/NewVersion/'
#PATH3 = 'xls/CompareResults/'
folder1 = os.listdir(path_ExcelOLD) # folder containing your files
#folder2 = os.listdir(path_ExcelNEW) # folder containing your files
#folder3 = os.listdir(PATH3) # folder containing your files

from flask import Flask
from flask import request

app = Flask(__name__)
#global accounted_dr

@app.route("/")
def index():
    currency_code = request.args.get("currency_code", "")
    #accounting_date =  "2021-06-16"
    accounting_date = request.args.get("accounting_date", "")
    user_je_source_name = request.args.get("user_je_source_name", "")
    category = request.args.get("category", "")
    #global accounted_dr
    accounted_dr = ""
    accounted_cr = ""
    journal_debit = ""
    journal_credit = ""
    debit_msg = ""
    credit_msg = ""
    #print("=====date====", accounting_date)
    # parts = accounting_date.split('-')
    # year = parts[0]
    # month = parts[1]
    # dd = parts[2]
    # str1 = year + month + dd
    # print(str1)

    print("currency code", currency_code)
    print("accounting date", accounting_date)
    print("user je source name", user_je_source_name)

    #accounting_date = accounting_date.replace('-', '')
    if currency_code:
       # date_string = str(accounting_date)
        #print("date_string =", date_string)

       # accounting_date1 = time.strftime(str(accounting_date), "%Y%m%d")
        #print("date_object =", accounting_date1)

        #accounting_date = re.sub('-', '', accounting_date)
       # Print as a string
        #accounting_date = str(accounting_date).replace("-", "")
        #print(str(accounting_date).replace("-", ""))
       # Print as an integer
        accounting_date = int(str(accounting_date).replace("-", ""))
        accounted_dr = getT24DB(currency_code,accounting_date, user_je_source_name)
        accounted_cr = getT24CR(currency_code, accounting_date, user_je_source_name)
        journal_debit = getOGLT24JournalDebit(currency_code, accounting_date, user_je_source_name, category)
        journal_credit = getOGLT24JournalCredit(currency_code, accounting_date, user_je_source_name, category)
        debit_msg =  compareDebit(accounted_dr,journal_debit)
        credit_msg =  compareCredit(accounted_cr,journal_credit)
       # print(accounted_dr)
        #test = test(test)
        #parsing date


        #accounting_date1 = accounting_date.replace('-', '')
        print("currency code",currency_code)
        print("accounting date",accounting_date)
        print("user je source name", user_je_source_name)
        print("category", category)
        #print("user je source name", user_je_source_name)
        #print("user je source name", user_je_source_name)
    else:
        currency_code = ""
    return (
        # USER JE SOURCE NAME: <input type="text" name="user_je_source_name">
        # DATE: <input type="DATE" name="accounting_date">
        """<form action="" method="get">
               
            
                <label for="user_je_source_name">Choose a user je source name:</label>
                <select name="user_je_source_name" id="user_je_source_name">
                  <option value="T24_UKC">T24_UKC</option>
            
                  
                </select>
                DATE: <input type="Date" name="accounting_date">
              
                <label for="currency_code">Choose a Currency code:</label>
                <select name="currency_code" id="currency_code">
                  <option value="AED">AED</option>
                  <option value="USD">USD</option>
                  <option value="SEK">SEK</option>
                  <option value="JPY">JPY</option>
                  <option value="EUR">EUR</option>
                  <option value="CHF">CHF</option>
                  <option value="AUD">AUD</option>
                  <option value="CAD">CAD</option>
                  <option value="GBP">GBP</option>
                </select>
                <!--<input type="submit" value="Calculate Accounted Debit">-->
                
                <br>
                  <label for="user_je_source_name">Choose a user je source name:</label>
                <select name="user_je_source_name" id="user_je_source_name">
                  <option value="T24_UKC">T24_UKC</option>
            
                  
                </select>
                DATE: <input type="Date" name="accounting_date">
              
                <label for="currency_code">Choose a Currency code:</label>
                <select name="currency_code" id="currency_code">
                  <option value="AED">AED</option>
                  <option value="USD">USD</option>
                  <option value="SEK">SEK</option>
                  <option value="JPY">JPY</option>
                  <option value="EUR">EUR</option>
                  <option value="CHF">CHF</option>
                  <option value="AUD">AUD</option>
                  <option value="CAD">CAD</option>
                  <option value="GBP">GBP</option>
                </select>
           
               <!--<input type="submit" value="Calculate Accounted Credit">-->
                </br>
                <br>
                  <label for="user_je_source_name">Choose a user je source name:</label>
                <select name="user_je_source_name" id="user_je_source_name">
                  <option value="T24_UKC">T24_UKC</option>
            
                  
                </select>
                DATE: <input type="Date" name="accounting_date">
              
                <label for="currency_code">Choose a Currency code:</label>
                <select name="currency_code" id="currency_code">
                  <option value="AED">AED</option>
                  <option value="USD">USD</option>
                  <option value="SEK">SEK</option>
                  <option value="JPY">JPY</option>
                  <option value="EUR">EUR</option>
                  <option value="CHF">CHF</option>
                  <option value="AUD">AUD</option>
                  <option value="CAD">CAD</option>
                  <option value="GBP">GBP</option>
                </select>
                <label for="category">Choose a category:</label>
                <select name="category" id="category">
                  <option value="Interface">Interface</option>
               <!--<input type="submit" value="Calculate Journal Debit">-->
                </br>
                
                  <br>
                  <label for="user_je_source_name">Choose a user je source name:</label>
                <select name="user_je_source_name" id="user_je_source_name">
                  <option value="T24_UKC">T24_UKC</option>
            
                  
                </select>
                DATE: <input type="Date" name="accounting_date">
              
                <label for="currency_code">Choose a Currency code:</label>
                <select name="currency_code" id="currency_code">
                  <option value="AED">AED</option>
                  <option value="USD">USD</option>
                  <option value="SEK">SEK</option>
                  <option value="JPY">JPY</option>
                  <option value="EUR">EUR</option>
                  <option value="CHF">CHF</option>
                  <option value="AUD">AUD</option>
                  <option value="CAD">CAD</option>
                  <option value="GBP">GBP</option>
                </select>
                <label for="category">Choose a category:</label>
                <select name="category" id="category">
                  <option value="Interface">Interface</option>
                <!--<input type="submit" value="Calculate Journal Credit">-->
                </br>
                <br>
               <input type="submit" value="Submit">
               <!--<input type="submit" value="Data Reconsilation Debit">-->
                </br>
                <br>
               <!--<input type="submit" value="Data Reconsilation Credit">-->
                
                
                </br>
            </form>"""
        + "<br>" +  "Accounted Debit: "
        + accounted_dr
        + "</br>"
        + "<br>" + "Accounted Credit: "
        + accounted_cr
        + "</br>"
        + "<br>" + "Journal Debit: "
        + journal_debit
        + "</br>"
        + "<br>" + "Journal Credit: "
        +  journal_credit
        + "<br>" + "Debit Compare Results: "
        + debit_msg
        + "</br>"
        + "<br>" + "Credit Compare Results: "
        + credit_msg
        + "</br>"


    )





def getT24DB(currency_code, accounting_date, user_je_source_name):

                df1 = pd.read_excel('T24SourceFile.xlsx', engine='openpyxl', header=0)
                #df1 = pd.read_excel('T24SourceFile.xlsx', engine='openpyxl', header=0)
                #df2 = pd.read_excel('OGLBatchFile.xlsx', engine='openpyxl', header=0)
                print(df1.head())

                list1 = []
               # print(df2.head())
                #df1.query(str("CURRENCY_CODE") == 'ÁED' and str("ACCOUNTING_DATE") == '20210130')
                #df1 = df1[df1["CURRENCY_CODE"] == 'AED']
                ##& (df1["ACCOUNTING_DATE"] == accounting_date)
                df1 = df1[(df1["CURRENCY_CODE"] == currency_code) & (df1["ACCOUNTING_DATE"] == accounting_date) & (df1["USER_JE_SOURCE_NAME"] == user_je_source_name)]
                #df2=  df1[df1["ACCOUNTING_DATE"] == '20210130']
                #df1 = df1[df1["ACCOUNTING_DATE"] == '20210130']
               # column = str("CURRENCY_CODE")
                # dump = dump.fillna(0)
                print(df1.head())
                df1 = df1.replace({'nan': 0.0}, regex=True)
                #finaldump = df1["CURRENCY_CODE"]

                finaldump_accounteddr = df1["ACCOUNTED_DR"]
                # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
                accounted_dr = 0.0
                for eachrow in finaldump_accounteddr:
                   print("hi")
                   print(accounting_date)
                   #print(eachrow.type())

                   accounted_dr = accounted_dr + eachrow
                   print(accounted_dr)
                #print('sum: ' + accounted_dr)

                return str(accounted_dr)


def getT24CR(currency_code, accounting_date, user_je_source_name):
    df1 = pd.read_excel('T24SourceFile.xlsx', engine='openpyxl', header=0)
    print(df1.head())
    list1 = []
    # print(df2.head())
    # df1.query(str("CURRENCY_CODE") == 'ÁED' and str("ACCOUNTING_DATE") == '20210130')
    # df1 = df1[df1["CURRENCY_CODE"] == 'AED']
    ##& (df1["ACCOUNTING_DATE"] == accounting_date)
    df1 = df1[(df1["CURRENCY_CODE"] == currency_code) & (df1["ACCOUNTING_DATE"] == accounting_date) & (df1["USER_JE_SOURCE_NAME"] == user_je_source_name)]

    # column = str("CURRENCY_CODE")
    # dump = dump.fillna(0)
    print(df1.head())
    df1 = df1.replace({'nan': 0.0}, regex=True)


    finaldump_accountedcr = df1["ACCOUNTED_CR"]
    # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
    accounted_cr = 0.0
    for eachrow in finaldump_accountedcr:
        accounted_cr = accounted_cr + eachrow
        print(accounted_cr)
    #print('sum: ' + str(accounted_cr))
    print(accounted_cr)
    return str(accounted_cr)


def getOGLT24JournalDebit(currency_code, date, user_je_source_name,category):
    # OGL DATA
    journal_name = user_je_source_name + "_" + str(date) + " " + category + " " + currency_code
    df2 = pd.read_excel('OGLBatchFile.xlsx', engine='openpyxl', header=0)
    df2.rename(columns={"Journal Name": "Journal_Name"}, inplace=True)
    df2.rename(columns={"Journal Credit": "Journal_Credit"}, inplace=True)
    df2.rename(columns={"Journal Debit": "Journal_Debit"}, inplace=True)
    list2 = []
   # s = "T24_UKC_20210131 Interface AED"
    df2 = df2[(df2["Journal_Name"] == journal_name)]

    finaldump_journaldebit = df2["Journal_Debit"]
    # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
    journal_debit = 0.0
    for eachrow in finaldump_journaldebit:
        journal_debit = journal_debit + eachrow
    #print('journal_debit: ' + str(journal_debit))


    return str(journal_debit)

def getOGLT24JournalCredit(currency_code, date, user_je_source_name,category):
    # OGL DATA
    journal_name = user_je_source_name + "_" + str(date) + " " + category + " " + currency_code

    df2 = pd.read_excel('OGLBatchFile.xlsx', engine='openpyxl', header=0)
    df2.rename(columns={"Journal Name": "Journal_Name"}, inplace=True)
    df2.rename(columns={"Journal Credit": "Journal_Credit"}, inplace=True)
    df2.rename(columns={"Journal Debit": "Journal_Debit"}, inplace=True)
    list2 = []
   # s = "T24_UKC_20210131 Interface AED"
    df2 = df2[(df2["Journal_Name"] == journal_name)]

    finaldump_journalCredit = df2["Journal_Credit"]
    # finaldump1 = pd.to_numeric(finaldump, errors='coerce')
    journal_credit = 0.0
    for eachrow in finaldump_journalCredit:
        journal_credit = journal_credit + eachrow
    #print('journal_credit: ' + str(journal_credit))


    return str(journal_credit)


def compareDebit(accounted_dr, journal_debit):
    if (accounted_dr == journal_debit):
        print("Data Match")
        strdebitMsg = "Data Match"
        return strdebitMsg
    else:
        #if (list1[1] == list2[0])
        strdebitMsg = "Data MisMatch"
        return strdebitMsg

def compareCredit(accounted_cr, journal_credit):
    print(accounted_cr)
    print(journal_credit)
    if (accounted_cr == journal_credit):
        print("Data Match")
        strcreditMsg = "Data Match"
        return strcreditMsg
    else:
        #if (list1[1] == list2[0])
        print("Data MisMatch")
        strcreditMsg = "Data MisMatch"
        return strcreditMsg



if __name__ == "__main__":
             app.run(host="127.0.0.1", port=8085, debug=True)

