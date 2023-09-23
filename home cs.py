# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:54:03 2023

@author: vong ly phung
"""

import os
os.mkdir('CS')
file_path = os.path.join('CS','homework.txt')
with open(file_path,'w')as file:
    file.write('4112044027_黃李鳳')
with open(file_path,'r')as file:
    content = file.read()
print("檔案內容:",content)
print("\n檔案資訊:")
print("資訊:",os.path.getsize(file_path),"bytes")
if os.path.exists('file_path.txt'):
    os.remove('file_path.txt')
    os.rmdir('CS')