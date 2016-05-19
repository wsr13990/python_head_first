import os

os.chdir('C:\Python Project\hfpy_code\chapter3')
data = open('sketch.txt')
for each_line in data:
    (role, line_spoken)= each_line.split(':',1)
    print(role, end='')
    print(' said ', end='')
    print(line_spoken, end='')
    
