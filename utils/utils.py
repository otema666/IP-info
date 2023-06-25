import requests

api_key = "f0b7f18a3e7541149ae064d21b443589"

def verificar(ip, tipo:str):
    url = f"https://vpnapi.io/api/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        match tipo:
            case "vpn":
                status = data['security']['vpn']
            case "pro":
                status = data['security']['proxy']
            case "tor":
                status = data['security']['tor']
            case "rel":
                status = data['security']['relay']
        if status:
            colour = "green"
        else:
            colour = "red"
        return f'<b style="color: {colour}">{str(status).upper()}</b>'
    except:
        return '<b style="color: red">FALSE</b>'  # No se está utilizando un tor node

def getIp():
    try:
        response = requests.get('https://ipapi.co/json')
        data = response.json()
        ip = data['ip']
        return ip
    except:
        return "False"
    
def getDetails(details, ipa):
    try:
        dall = details.all
    except:
        dall = "All info couldn't be collected"

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
        url_maps = f'https://google.com/maps/place/{loc}'
    except:
        url_maps = "No disponible"

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

    url_IP = f'https://whatismyipaddress.com/ip/{ipa}'



    # List
    all = []

    all.append(hostname) #0
    all.append(org)

    all.append(country)
    all.append(region)
    all.append(city)
    all.append(postal) #5
    all.append(timezone)
    all.append(loc)

    all.append(url_maps)
    all.append(url_IP)
    all.append(ipa) #10

    all.append(dall)
    return all