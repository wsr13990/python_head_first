import nester
import os

os.chdir('C:\python_head_first\hfpy_code\chapter3')
man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken)= each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print('The data file is missing')
try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')

    nester.print_lol(man, fh = man_file)
    nester.print_lol(other, fh = other_file)

except IOError:
    print('File Error')
finally:
    man_file.close()
    other_file.close()

