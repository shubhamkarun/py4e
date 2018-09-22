import urllib.request, urllib.parse, urllib.error
import json

service_url = "http://py4e-data.dr-chuck.net/geojson?"

while True:
    address = input("Enter address: ")
    if len(address)<1: break

    url = service_url + urllib.parse.urlencode({'address':address})
    print("Retrieving" ,url)
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    print("Retrived", len(data), "characters")
    js = json.loads(data)
    print(json.dumps(js, indent=4))
    id = js["results"][0]["place_id"]
    print(id)
