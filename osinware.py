from colorama import Fore
import pyfiglet
import json
import requests

print(Fore.GREEN+pyfiglet.figlet_format("OsinWare"), end="")
print(Fore.WHITE+"      :::[+] author: th3 want3d")
print(Fore.WHITE+"      :::[+] version: 1.0\n")

print(Fore.BLUE+"[1] find data from IP")
print(Fore.BLUE+"[2] whats my IP?\n")

api_key = "nokey"
menu_option = input(Fore.WHITE+"Choose an option > ")

def get_information_by_ip(api_key):
    ip_address = input(Fore.WHITE+"Enter target ip address > ")
    response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}')
    dictionary = json.loads(response.content)

    return dictionary

def get_information_of_my_ip(api_key):
    response = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey="+api_key)
    dictionary = json.loads(response.content)
    
    return dictionary['ip']

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


my_ip = get_information_of_my_ip(api_key)

if menu_option == "1":
    generate_table_result_by_ip(get_information_by_ip(api_key))
else:
    print(Fore.YELLOW+"#-------------"+generate_dynamic_dash(my_ip)+"---#")
    print(Fore.WHITE+"[+] your IP is: "+my_ip)
    print(Fore.YELLOW+"#-------------"+generate_dynamic_dash(my_ip)+"---#")