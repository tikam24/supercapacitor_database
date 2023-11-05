# -*- coding: utf-8 -*-
"""
Tool to download abstracts by using EID list in text files.

"""
import pandas as pd
import abstract_retrival as ar 
import openpyxl


MY_API_KEY = 'f73e832425664188550dd2d9ee12ec3d'              
serial_number = 1


df = pd.read_excel('abstracts_details.xlsx', engine='openpyxl')


newdf, sn, li = ar.abstract_scraper("eid2.txt", MY_API_KEY ,serial_number)
 
   
with open('eid2.txt', 'w') as f1:
    f1.write(li)

df1 = df._append(newdf)

df1.to_excel('abstracts_details.xlsx', engine ='openpyxl')
  
print('Next Serial Number:', sn)