import urllib.request
import json
import requests

text = input("Masukkan text yang ingin di enkripsi : ")

dataEncrypt = {
    "text" : text
}
# jsonData = urllib.request.urlopen(f"http://localhost/RemoteInvocation/enkripsiString.php?text={text}")
jsonData = requests.post("http://localhost/RemoteInvocation/enkripsiString.php", data=dataEncrypt)

data = json.loads(jsonData.text)
print(data["text-encrypt"])