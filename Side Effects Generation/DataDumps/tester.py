# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:04:58 2017

@author: saiav
"""

import os
import re 
import io 

ls = list()

f = open('test.txt')

for line in f:
    ls = re.findall('[a-zA-Z0-9 ]*effect',line,re.IGNORECASE)
    if len(ls)>0:
        print(line)
        


ls = list()
#with codecs.open(pathWikiXML, "w", ENCODING) as articlesFH:                
for filename in os.listdir(r'C:\Users\saiav\Desktop\UNCC\MDS\Project\DataDumps'):
    if filename.endswith('.txt'):
        textfile = open(filename,encoding = 'utf8')
        buffer = []
        for line in textfile:
            ls = re.findall('[a-zA-Z0-9 ]*effect',line,re.IGNORECASE)
            if len(ls) > 0:
                buffer.append(nline)
        else: 
            filename = filename.replace('.txt','')
            fu = open(filename+"_sideeffects.txt", "w+")
                with io.open(filename+"_sideeffects.txt", "w", encoding="utf-8") as fu:
                    buff_string = '\n \n'.join(map(str,buffer) )
                    fu.write(buff_string)
                    fu.close()
                    buffer=[]
                    buff_string = ''
                    print('try:'+filename)
                    break
                        buffer.append(nline)
        textfile.close()
                     
