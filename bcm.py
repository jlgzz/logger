import requests

url="http://192.168.1.1/ports.jsn"

r=requests.get(url)

if  __name__=="__main__":
    print(r.json())