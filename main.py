import ipinfo
import pprint
from colorama import init, Fore, Style
import requests
import os
import webbrowser



# Inicializar colorama
init()

# Functions
def hueco():
    print()
    print("--------------------")
    print()

def espacio():
    for a in range(24):
            print(Fore.GREEN + "-" + Style.RESET_ALL, end="", flush=True)
            print(Fore.RED + "-" + Style.RESET_ALL, end="", flush=True)  
            print(Fore.BLUE + "-" + Style.RESET_ALL, end="", flush=True)
            print(Fore.YELLOW + "-" + Style.RESET_ALL, end="", flush=True)
            print(Fore.MAGENTA + "-" + Style.RESET_ALL, end="", flush=True)

def obtener_direccion_ip():
    try:
        response = requests.get('https://ipapi.co/json')
        data = response.json()
        ip = data['ip']
        return ip
    except:
        return False

def verificar_vpn(ip):
    api_key = "f0b7f18a3e7541149ae064d21b443589"
    url = f"https://vpnapi.io/api/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        vpn_status = data['security']['vpn']
        return vpn_status
    except:
        return False  # No se está utilizando una VPN

def verificar_proxy(ip):
    api_key = "f0b7f18a3e7541149ae064d21b443589"
    url = f"https://vpnapi.io/api/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        proxy_status = data['security']['proxy']
        return proxy_status
    except:
        return False  # No se está utilizando un proxy

def verificar_tor(ip):
    api_key = "f0b7f18a3e7541149ae064d21b443589"
    url = f"https://vpnapi.io/api/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        tor_status = data['security']['tor']
        return tor_status
    except:
        return False  # No se está utilizando un tor node

def verificar_relay(ip):
    api_key = "f0b7f18a3e7541149ae064d21b443589"
    url = f"https://vpnapi.io/api/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        relay_status = data['security']['relay']
        return relay_status
    except:
        return False  # No se está utilizando un relay de apple




access_token = '13e422b8b69e59'
handler = ipinfo.getHandler(access_token)
print(f'{Fore.MAGENTA}Welcome to IP info by otema     {Fore.LIGHTBLACK_EX}(type "mine" to select your current ip){Fore.RESET}')
print(f'{Fore.LIGHTWHITE_EX}IP: {Fore.RESET}', end="")
IP = str(input()).lower()
if IP == "all":
    print(f'{Fore.LIGHTBLACK_EX}-- All info unlocked!{Fore.RESET}')
    all_info = True
    IP = str(input("IP: "))
else:
    all_info = False

if IP == "mine":
    IP = obtener_direccion_ip()
    if IP == False:
        print(f'{Fore.RED}[!]{Fore.RESET} Error al obtener tu dirección IP, comprueba tu conexión a internet e inténtalo de nuevo')
        exit()
else:
    pass

details = handler.getDetails(IP)

# Vars
VPN = verificar_vpn(IP)
proxy = verificar_proxy(IP)
tor = verificar_tor(IP)
relay = verificar_relay(IP)

try:
    ALL = details.all
except:
    ALL = "all info couldn't be collected"

try:
    hostname = details.hostname
except:
    hostname = "No encontrado"

try:
    city = details.city
except:
    city = "No encontrada"

try:
    region = details.region
except:
    region = "No encontrada"

try:
    country = details.country
except:
    country = "No encontrada"

try:
    loc = details.loc
except:
    loc = "No encontrada"

try:
    org = details.org
except:
    org = "No encontrada"

try:
    postal = details.postal
except:
    postal = "No encontrado"

try:
    timezone = details.timezone
except:
    timezone = "No encontrada"

if loc != "No encontrada":
    url_maps = f'https://google.com/maps/place/{loc}'
else:
    url_maps = "No disponible"

url_IP = f'https://whatismyipaddress.com/ip/{IP}'

# List
all = []

all.append(hostname)
all.append(city)
all.append(region)
all.append(country)
all.append(loc)
all.append(org)
all.append(postal)
all.append(timezone)

# OUTPUT
os.system('cls')
espacio()
print(f'                                               {Fore.LIGHTWHITE_EX}Información de {Fore.RED}{IP}{Fore.LIGHTWHITE_EX}.{Fore.RESET}')
espacio()
print(" ")

print()


print(f'{Fore.CYAN}Información básica:')
print()
print(f'{Fore.YELLOW}Hostname:     {Fore.GREEN}{hostname}')
print(f'{Fore.YELLOW}Organización: {Fore.GREEN}{org}')
print()
print(f'{Fore.CYAN}Seguridad:')
print()
if VPN:
    print(f'{Fore.YELLOW}VPN:          {Fore.GREEN}{VPN}')
else:
    print(f'{Fore.YELLOW}VPN:          {Fore.RED}{VPN}')

if proxy:
    print(f'{Fore.YELLOW}Proxy:        {Fore.GREEN}{proxy}')
else:
    print(f'{Fore.YELLOW}Proxy:        {Fore.RED}{proxy}')

if tor:
    print(f'{Fore.YELLOW}Tor:          {Fore.GREEN}{tor}')
else:
    print(f'{Fore.YELLOW}Tor:          {Fore.RED}{tor}')

if relay:
    print(f'{Fore.YELLOW}Relay:        {Fore.GREEN}{relay}')
else:
    print(f'{Fore.YELLOW}Relay:        {Fore.RED}{relay}')


print()
print(f'{Fore.CYAN}Geolocalización:')
print()
print(f'{Fore.YELLOW}País:         {Fore.GREEN}{country}{Fore.RESET}')
print(f'{Fore.YELLOW}Región:       {Fore.GREEN}{region}{Fore.RESET}')
print(f'{Fore.YELLOW}Ciudad:       {Fore.GREEN}{city}{Fore.RESET}')
print(f'{Fore.YELLOW}CP:           {Fore.GREEN}{postal}{Fore.RESET}')
print(f'{Fore.YELLOW}Zona Horaria: {Fore.GREEN}{timezone}{Fore.RESET}')
print(f'{Fore.YELLOW}Google Maps:  {Fore.BLUE}{url_maps}{Fore.RESET}')
print()
print(f'{Fore.CYAN}Otros servicios:')
print()
print(f'{Fore.YELLOW}Enlace a whatismyipaddress: {Fore.BLUE}{url_IP}{Fore.RESET}')

if all_info:
    print()
    print(f'{Fore.CYAN}All info:{Fore.LIGHTBLACK_EX}')
    print()
    pprint.pprint(details.all)

print()
espacio()
print()

while True:
    print(f'Quieres abrir algún enlace? ({Fore.GREEN}s{Fore.RESET}/{Fore.RED}n{Fore.RESET}) --> ', end="")
    r = str(input()).lower()
    if r == "s":
        print(f'{Fore.GREEN}    1. {Fore.LIGHTWHITE_EX}Google Maps')
        print(f'{Fore.GREEN}    2. {Fore.LIGHTWHITE_EX }Whatismyipaddress')
        print(f'{Fore.GREEN}    3. {Fore.LIGHTWHITE_EX}Todo{Fore.RESET}')
        print()
        print(f'Respuesta: {Fore.BLUE}', end="")
        nav = int(input())
        print(Fore.RESET)
        if nav == 1:
            webbrowser.open(url_maps)
            exit()
        elif nav == 2:
            webbrowser.open(url_IP)
            exit()
        elif nav == 3:
            webbrowser.open(url_maps)
            webbrowser.open(url_IP)
            exit()
        else:
            print(f'{Fore.RESET}Respuesta no válida')
            print()
    elif r == "n":
        exit()
    else:
        print("Respuesta no válida")