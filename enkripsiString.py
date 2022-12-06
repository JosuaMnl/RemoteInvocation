import urllib.request
import json
import requests

text = input("Masukkan text yang ingin di enkripsi : ")

dataEncrypt = {
    "text" : text
}
# print(json.dumps(dataEncrypt))
# jsonData = urllib.request.urlopen(f"http://localhost/RemoteInvocation/enkripsiString.php?text={text}")
jsonData = requests.post("http://localhost/RemoteInvocation/enkripsiString.php", data=dataEncrypt)
print(type(jsonData.text))
# print(jsonData.text)
# # print(jsonData.text["text-encrypt"])
# data = json.load(jsonData.json)
data = dict(data=jsonData.text )
data = data["data"]
# print(data["text-encrypt"])

# print(data)
# print(data["text-encrypt"])