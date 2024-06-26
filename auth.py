from colorama import Fore
import json
import requests

def onsuccess(api_key):
    file = open("osinware.conf", mode="w")

    file.write("api_key:"+api_key)

    result = f'{Fore.YELLOW}[+] Your access key has been generated successfully, see it in osinware.conf file'

    return result

def onerror(error):
    result = f'{Fore.RED}[!] {error}'

    return result

def verify_array_keys(data):
    for key in data:
        if key == "api_key":
            return onsuccess(data["api_key"])
        elif key == "error":
            return onerror(data["error"])

def create_account(username, password):
    response = requests.post("http://localhost:8000/api/auth/register.php", data={"username": username, "password": password})
    
    dictionary = json.loads(response.content)
    
    return verify_array_keys(dictionary["content"])

def login(username, password):
    response = requests.post("http://localhost:8000/api/auth/login.php", data={"username": username, "password": password})
    
    dictionary = json.loads(response.content)

    return verify_array_keys(dictionary["content"])