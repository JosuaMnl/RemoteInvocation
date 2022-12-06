import urllib.request
import json
import requests

text = input("Masukkan text yang ingin di enkripsi \t: ")

dataEncrypt = {
    "text" : text
}
# jsonData = urllib.request.urlopen(f"http://localhost/RemoteInvocation/enkripsiString.php?text={text}")
jsonData = requests.post("http://sister.namekbuat.com/si7a/enkripsiString.php", data=dataEncrypt)

data = json.loads(jsonData.text)
print(f"Hasil dari enkripsi \t\t\t: {data['text-encrypt']}")
print(data)