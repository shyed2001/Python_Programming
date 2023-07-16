import netifaces
import urllib.request

TEST_URL = 'http://www.google.com'

def get_active_interface():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            return interface
    raise ValueError("No active network interface.")

def is_wifi_connected():
    interface = get_active_interface()
    return interface and "Wi-Fi" in interface

def is_lan_connected():
    interface = get_active_interface()
    return interface and ("Ethernet" in interface or "eth" in interface)

def has_internet_connection():
    try:
        urllib.request.urlopen(TEST_URL, timeout=1)
        return True
    except urllib.request.URLError:
        return False

if __name__ == '__main__':
    # Check network interfaces
    interfaces = [netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr'] for interface in netifaces.interfaces() if netifaces.AF_INET in netifaces.ifaddresses(interface)]
    print(f"Available interfaces: {interfaces}")
    
    # Check Wi-Fi and LAN connection
    try:
        interface = get_active_interface()
    except ValueError:
        print("No active network interface.")
    else:
        if is_wifi_connected():
            print("Connected to Wi-Fi.")
        elif is_lan_connected():
            print("Connected to LAN.")
        else:
            print("Not connected to any network.")
    
    # Check internet connectivity
    if has_internet_connection():
        print("Internet connection is active.")
    else:
        print("No internet connection.")
