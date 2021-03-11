# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 10:07:55 2021

@author: Gabriel
"""

from bs4 import BeautifulSoup
import requests
from collections import Counter
import time
# url1 = 'https://biblija.ks.hr/knjiga-postanka/1'
# url2 = 'https://hr.wikipedia.org/wiki/Sepultura'
# url3 = 'https://www.stocitas.org/anarhosindikalizam.htm'
filename = 'croatian.txt'
def start(url,arg):
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    wordlist = []
    clean_list = []


    for each_text in soup.findAll(arg):
        content = each_text.text
        words = content.lower().split()
        
        for each_word in words: 
            wordlist.append(each_word) 
                
        for word in wordlist:
            symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/.,>>»«– '
                        
            for i in range(len(symbols)):
                word = word.replace(symbols[i], '')
            
            if len(word) > 0:
                clean_list.append(word)
                
    for word in clean_list:
            if any(char.isdigit() for char in word):
                clean_list.remove(word)
            
    return clean_list
            

def append_to_dict(dictionary,clean_wordlist):
    
    for word in clean_wordlist:
        if word in dictionary:
            dictionary[word] += 1
    
    return dictionary

def create_dict(filename):

    with open(filename, 'r',encoding='utf-8') as read_obj:
        myList = []
        myDict = {}
        for line in read_obj:
            myList.append(line.strip('\n'))        
        for l in myList:
            myDict[l] = 0
            
    read_obj.close()
    return myDict


def save_data(dictionary,filename):
    with open(filename,'w',encoding='utf-8') as write_obj:
        write_obj.write(str(dictionary))
        
    write_obj.close()


f = open('url.txt','r')
urls = f.readlines()

myDict = create_dict(filename)
start_time = time.time()
  
for url in urls:
    lista = url.split()
    wordlist = start(lista[0],lista[1])
    append_to_dict(myDict, wordlist)
    save_data(myDict,'data.txt')

print("--- %s seconds ---" % (time.time() - start_time)) 
c = Counter(myDict)
top = c.most_common(100)
g = open('top100.txt','w',encoding='utf-8') 
g.write(str(top))
print(top)    
f.close()
        
# if __name__ == '__main__':
#     f = open('url.txt','r')
#     urls = f.readlines()
#     myDict = create_dict(filename)
    
#     for url in urls:
#         wordlist = start(url)
#         append_to_dict(myDict, wordlist)
#         save_data(myDict,'data.txt')
    
#     f.close()