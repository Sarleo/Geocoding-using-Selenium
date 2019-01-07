# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 20:55:14 2018

@author: saranshmohanty
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os
# mention your own directory
os.chdir('C:/Users/saranshmohanty/Desktop/')
driver=webdriver.Firefox()# change this line of code if you are using any other webdriver
df=[]
########################################multiple addresses###############################
#mention your csv file
df=pd.read_csv('add.csv')
fd=df.Address
fdf=fd.values
final=[]
#driver.get("https://www.google.com/maps/@20.9880134,73.7876856,5z")
driver.get("https://www.google.com/maps/")
for ii in fdf:
    #driver.get("https://www.google.com/maps/")
    elem2= driver.find_element_by_css_selector("#searchboxinput")
    count = 0
    elem2.clear()
    elem2.send_keys(ii)
    elem2.send_keys(Keys.ENTER)
    time.sleep(6)
    elem3=driver.current_url
    for i in range (len(elem3)):
        if elem3[i]=="@":
            break
    for j in range(i,len(elem3)):
        if(elem3[j]==","):
            count+=1
        if (count == 2):
            break;
    S=elem3[i+1:j]
    print(len(final))
    #print(S)
    coord=[]
    lat,long=S.split(",")
    final.append((ii,lat,long))
   
final_panda=[]
final_panda=pd.DataFrame(list(final))
final_panda.columns=['Address','lat','long']
final_panda.to_csv('latlong 2list.csv',index=False)

########################################################single entry############################
driver.get("https://www.google.com/maps/")
elem2= driver.find_element_by_css_selector("#searchboxinput")
count = 0
elem2.clear()
elem2.send_keys("kempfort mall bangalore")#sample input
elem2.send_keys(Keys.ENTER)
elem3=driver.current_url
for i in range (len(elem3)):
    if elem3[i]=="@":
        break
for j in range(i,len(elem3)):
    if(elem3[j]==","):
        count+=1
    if (count == 2):
        break;
S=elem3[i+1:j]
lat,long=S.split(",")
final.append((i,lat,long))
driver.close()

# it is important to execute driver.close() to avoid any stale elements in the next run
