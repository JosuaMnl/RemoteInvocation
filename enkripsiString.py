import urllib.request
import json

text = input("Masukkan text yang ingin di enkripsi : ")
jsonData = urllib.request.urlopen(f"http://localhost/RemoteInvocation/enkripsiString.php?text={text}")

data = json.load(jsonData)

print(data)
print(data["text-encrypt"])