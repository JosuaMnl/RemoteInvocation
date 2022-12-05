import urllib.request
import json

jsonData = urllib.request.urlopen("http://localhost:9999/yosha10/tes.php")

data = json.load(jsonData)

print(data)
print(data["angka"])