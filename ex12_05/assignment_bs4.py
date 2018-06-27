import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# for dealing with ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


data=list()
url = input('Enter-')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

# Retrive all of the anchor tags
tags = soup('span')
for tag in tags:
    num=tag.contents
    num=list(map(int,num))
    data=data+num


print(data)
print(num)
print('count ',len(data))
print('sum ',sum(data))
