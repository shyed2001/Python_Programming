import psutil
import urllib.request
import os

def get_network_interface():
    interfaces = psutil.net_if_stats().keys()
    for interface in interfaces:
        stats = psutil.net_if_stats()[interface]
        if stats.isup and stats.speed > 0:
            return interface
    return None

def is_wifi_connected():
    interface = get_network_interface()
    return interface and interface.startswith('w')

def is_lan_connected():
    interface = get_network_interface()
    return interface and (interface.startswith('e') or interface.startswith('eth'))

def has_internet_connection():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.request.URLError:
        return False

interfaces = psutil.net_if_stats().keys()
print("Available interfaces:", interfaces)

if __name__ == '__main__':
    if is_wifi_connected():
        print("Connected to Wi-Fi.")
    elif is_lan_connected():
        print("Connected to LAN.")
    else:
        print("Not connected to any network.")

    if has_internet_connection():
        print("Internet connection is active.")
    else:
        print("No internet connection.")
