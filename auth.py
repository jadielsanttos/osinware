import json
import requests

def create_account(username, password):
    response = requests.post("http://localhost:8000/api/auth/register.php", data={"username": username, "password": password})
    
    dictionary = json.loads(response.content)
    
    return verify_array_keys(dictionary)

def login(username, password):
    response = requests.post("http://localhost:8000/api/auth/login.php", data={"username": username, "password": password})
    
    dictionary = json.loads(response.content)

    return verify_array_keys(dictionary)

def verify_array_keys(data):
    for key in data['content']:
        if key == 'api_key':
            return "[+] your api key: "+data['content']['api_key']
        elif key == 'error':
            return "[!] "+data['content']['error']