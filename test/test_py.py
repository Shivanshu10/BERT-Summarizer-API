import requests

url = 'http://127.0.0.1:5000/'
param = {'somekey': 'somevalue'}

x = requests.post(url, json=param)
#x = requests.get(url)
print(x.text)
print(x.status_code)