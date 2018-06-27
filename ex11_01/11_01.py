
import re
file = input('Enter a file name:')
if len(file) < 1 : file = 'actual_file.txt'
handle = open(file)
num_list=list()
for line in handle:
        stuff = re.findall('[0-9]+',line)
        if len(stuff) == 0 : continue
        #print(stuff)
        stuff = list(map(int,stuff))
        num_list = num_list+stuff
        #print(num_list)
print (len(num_list))
print (sum(num_list))
