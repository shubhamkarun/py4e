import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter url:")
handle = urllib.request.urlopen(url)
data = handle.read().decode()

js = json.loads(data)
print(json.dumps(js, indent=4))


total = 0
#json is a dictionary which in turn contains list of dictionaries in itself.
#First store the list in an object and then parse the count values from the dictionaries in the list
js=js["comments"]
for counts in js:
    print(int(counts["count"]))
    total += int(counts["count"])
    print(total)
