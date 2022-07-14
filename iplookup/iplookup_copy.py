from requests import get

def get_ip():
    response = get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def iplookup():
    ip_address = get_ip()
    response = get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    print(location_data)
    return location_data