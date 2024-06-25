from colorama import Fore
import json
import requests

def get_information_by_ip(api_key):
    ip_address = input(Fore.WHITE+"Enter target ip address > ")

    response = requests.get(f'http://localhost:8000/api/webservices/ipgeolocation/get.php?ip={ip_address}&api_key={api_key}')

    dictionary = json.loads(response.content)

    if verify_array_keys(dictionary['content']) != None:
        print_error(verify_array_keys(dictionary['content']))
        return

    return generate_table_result_by_ip(dictionary['content'])

def generate_dynamic_dash(value):
    string = ""

    for _ in range(0, len(value)):
        string = "-" * int(len(value))

    return string

def generate_table_result_by_ip(ip_data):
    coords = ip_data['latitude']+","+ip_data['longitude']

    print(Fore.YELLOW+"#----------"+generate_dynamic_dash(coords)+"---#")
    print(Fore.WHITE+"[+] ip: "+ip_data['ip'])
    print(Fore.WHITE+"[+] isp: "+ip_data['isp'])
    print(Fore.WHITE+"[+] coords: "+coords)
    print(Fore.WHITE+"[+] country: "+ip_data['country_name'])
    print(Fore.WHITE+"[+] city: "+ip_data['city'])
    print(Fore.WHITE+"[+] calling code: "+ip_data['calling_code'])
    print(Fore.WHITE+"[+] currency: "+ip_data['currency']['name'])
    print(Fore.WHITE+"[+] capital: "+ip_data['country_capital'])
    print(Fore.YELLOW+"#----------"+generate_dynamic_dash(coords)+"---#")

def verify_array_keys(data):
    for key in data:
        if key == 'error':
            return data['error']
        elif key == 'message':
            return data['message']
    
def print_error(error):
    print(Fore.RED+"[!] "+error)