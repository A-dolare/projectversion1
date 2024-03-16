# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:12:25 2024

@author: 91915
"""
import csv 
from gmplot import gmplot

with open('route.csv','r') as f: # here we are opening the csv file in read mode
    reader=csv.reader(f) # reader function makes an iterator and then you can iterate over each element as a list
    
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        print(lat)
        print(long)
        print(lat+long)
        