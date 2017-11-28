# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:33:31 2017

@author: saiav
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:35:36 2017

@author: saiav
"""

import re
import os 
import codecs
import csv
import time
import io 

PATH_WIKI_XML = r'C:\Users\saiav\Desktop\UNCC\MDS\Side_effects'
FILENAME_WIKI = 'drugs_full_xml.xml'
ENCODING = "utf-8"
pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)



f = open('drugs_full_xml.xml', encoding = "utf8")

count = 0
for line in f:
    #ls = line.rstrip()
    ls = re.findall('^==[a-zA-Z0-9 ]*effects+==',line, re.IGNORECASE)
    if len(ls) > 0:
        while True:
            nline = f.readline()
            if len(re.findall('^==+[a-zA-Z0-9 ]*effects+==+',nline,re.IGNORECASE))>0:
                continue
            elif len(re.findall('^==',nline))>0:
                count+=1
                break
            else: 
                print(nline)
                

ls = list()
#with codecs.open(pathWikiXML, "w", ENCODING) as articlesFH:                
for filename in os.listdir(r'C:\Users\saiav\Desktop\UNCC\MDS\Project\DataDumps'):
    if filename.endswith('.txt'):
        textfile = open(filename,encoding = 'utf-8')
        buffer = []
        for line in textfile:
            ls = re.findall('^&lt;!--[a-zA-Z0-9 ]*effect+',line, re.IGNORECASE)
            if len(ls) > 0:
                print('if ls'+filename)
                while True:
                    nline = textfile.readline()
                    if len(re.findall('^&lt;!--[a-zA-Z0-9 ]*effect+',nline,re.IGNORECASE))>0:
                        print('if re:'+filename)
                        continue
                    elif len(re.findall('^&lt;!--',nline))>0:
                        try:
                            if len(buffer) is not 0:
                                fu = open(filename+"_sideeffects.txt", "w+")
                                with io.open(filename+"_sideeffects.txt", "w", encoding="utf-8") as fu:
                                    buff_string = '\n \n'.join(map(str,buffer) )
                                    fu.write(buff_string)
                                    fu.close()
                                    buffer=[]
                                    buff_string = ''
                                    print('try:'+filename)
                                    break
                        except:
                            print('except:'+filename)
                            break                
                    else: 
                        buffer.append(nline)
        textfile.close()
             
    
    

for line in openfile:
    check_line = re.findall('',line,re.IGNORECASE)    

for filename in os.listdir(r'C:\Users\saiav\Desktop\UNCC\MDS\Project\DataDumps'):
    if filename.endswith('.txt'):
        print(filename)
    else:
        continue

  
          
        #print([f.readline() for i in range(4)])
import csv 
with open('articles.csv', newline= '', encoding= 'utf8') as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        print(row['title'])