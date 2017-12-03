# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:35:36 2017

@author: saiav
"""
from xml.dom import minidom
import re 
ls = list()
f = open('drugs_full_xml.xml', encoding = "utf8")


for line in f:
    #ls = line.rstrip()
    ls = re.findall('^==[a-zA-Z0-9 ]*Effects+==',line)
    if len(ls) > 0:
        while True:
            nline = f.readline()
            if len(re.findall('^==+[a-zA-Z0-9 ]*effects+==+',nline))>0:
                continue
            elif len(re.findall('^==',nline))>0:
                break
            else: 
                print(nline)
            
            
        #print([f.readline() for i in range(4)])