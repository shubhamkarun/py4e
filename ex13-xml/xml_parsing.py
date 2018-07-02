import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location:')
print('Retrieving:',url)
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
stuff = tree.findall('comments/comment')
print('count = ', len(stuff))

lst=list()
for items in stuff:
    counts=int(items.find('count').text)
    lst.append(counts)

#print(lst)
Sum = sum(lst)
print(Sum)
