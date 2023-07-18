import psutil
import netifaces
import socket
import urllib.request
import subprocess
import re


def get_network_adapters():
    """Gets the list of network adapters."""
    process = subprocess.Popen(["ipconfig", "/all"], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    return output.decode("utf-8")


def is_wifi(adapter):
    """Checks if the adapter is connected to WiFi."""
    return "Wireless LAN adapter" in adapter


def is_ethernet(adapter):
    """Checks if the adapter is connected to Ethernet."""
    return "Ethernet adapter" in adapter


def main():
    """Checks if the computer is connected to WiFi or Ethernet."""
    adapters = get_network_adapters()
    for adapter in adapters.splitlines():
        if is_wifi(adapter):
            print("You are connected to WiFi.")
            break
      
        elif is_ethernet(adapter):
            print("You are connected to Ethernet.")
            break
        else:
            print("You are not connected to any network.")


if __name__ == "__main__":
    main()
