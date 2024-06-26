from colorama import Fore
import pyfiglet
import auth
import ipgeolocation

print(Fore.GREEN+pyfiglet.figlet_format("OsinWare"), end="")
print(Fore.WHITE+"       :::[+] author: Th3 Want3d")
print(Fore.WHITE+"       :::[+] version: 1.0.1\n")

print(Fore.WHITE+"[!] Welcome! create account or make login to get your access key...\n")
print(Fore.YELLOW+"[1] create account")
print(Fore.YELLOW+"[2] login")
print(Fore.YELLOW+"[3] IP information gathering\n")

menu_option = input(Fore.WHITE+"Choose an option > ")

def create_account(username, password):
    return auth.create_account(username, password)

def login(username, password):
    return auth.login(username, password)

def start(menu_option):
    username = input(Fore.WHITE+"Enter username > ")
    password = input(Fore.WHITE+"Enter password > ")

    if menu_option == '1':
        return create_account(username, password)
    elif menu_option == '2':
        return login(username, password)
    
def get_data_by_target_ip():
    file = open("osinware.conf", mode="r")

    api_key = file.read().split(":")[1]

    ipgeolocation.get_information_by_ip(api_key)

if menu_option == '1' or menu_option == '2':
    print(start(menu_option))
elif menu_option == '3':
    get_data_by_target_ip()
else:
    print(Fore.RED+"[!] Sorry, invalid option...")
    