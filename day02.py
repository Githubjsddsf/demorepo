# basic authentication

import json

file = open("secrets.json", "r")
data = file.read()
file.close()
print(data)

auth = json.loads(data)

username = input("Adja meg a felhasználónevét:")
password = input("Adja meg a jelszavát:")

if username == auth["username"] and password == auth["password"]:
    print("Üdv a fedélzeten!")

else 
    print("A belépés nincs engedélyezve!")