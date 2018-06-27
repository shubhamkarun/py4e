import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# for dealing with ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter-')
pos = int(input('Enter position:'))- 1
count = int(input('Enter count:'))
singlelink = list()
singlelink.append(url)

print('Retrieving: ',singlelink[0])

for i in range(count):
    html = urllib.request.urlopen(singlelink[-1]).read()
    soup = BeautifulSoup(html,'html.parser')
# Retrive all of the anchor tags
    linklist = list()
    tags = soup('a')
    for tag in tags:
        #print(pos)
        linklist.append(tag)
        #print(linklist)
    url = linklist[pos].get('href',None)
    #print(links)
    print('Retrieving: ',url)
    singlelink.append(url)
print('Last url: ',singlelink[-1])
