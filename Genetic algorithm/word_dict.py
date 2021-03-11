# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:49:14 2021

@author: Gabriel
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

""" ------------------------------------ """
""" Stvaranje Dicta sa hrvatskim rječima """
""" ------------------------------------ """

filename = r'croatian1.txt'
with open(filename, 'r',encoding='utf-8') as read_obj:
    myList = []
    myDict = {}
    for line in read_obj:
        myList.append(line.strip('\n'))        
    for l in myList:
        myDict[l] = 0
    
        


""" ---------------------------------------- """
""" Popunjavanje dicta sa hrvatskim riječima """
""" ---------------------------------------- """

myDict['bog'] = 0
myDict['je'] = 0


f = open('url.txt','r')
urls = f.readlines()
for url in urls:
    
    page = urlopen(url)
    html = page.read()
    
    for k in myDict:
        
        searched_word = k
        searched_word_capitalized = k.capitalize()
        soup = BeautifulSoup(html,'html.parser')
        results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
        results_capitalized = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word_capitalized)), recursive=True)
        myDict[k] += len(results)
        myDict[k] += len(results_capitalized)
   
        
   
    
with open('data.txt','w',encoding='utf-8') as write_obj:
    write_obj.write(str(myDict))
    
print(myDict)
f.close()
read_obj.close()
write_obj.close()  





