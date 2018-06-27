
#using urllib to access web data but only works for http websites i guess !!

import urllib.request , urllib.parse , urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())
