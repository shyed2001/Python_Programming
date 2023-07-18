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
    """Checks if the adapter is a WiFi adapter."""
    return "Wireless LAN adapter" in adapter


def is_ethernet(adapter):
    """Checks if the adapter is an Ethernet adapter."""
    return "Ethernet adapter" in adapter


def has_default_gateway(adapter):
    """Checks if the adapter has a default gateway assigned."""
    return "Default Gateway" in adapter


def get_ipv4_address(adapter):
    """Extracts the IPv4 address from the adapter information."""
    match = re.search(r"IPv4 Address[.\s]*: ([^\r\n]+)", adapter)
    if match:
        return match.group(1)
    return None


def get_ipv6_address(adapter):
    """Extracts the IPv6 address from the adapter information."""
    match = re.search(r"IPv6 Address[.\s]*: ([^\r\n]+)", adapter)
    if match:
        return match.group(1)
    return None


def get_default_gateway(adapter):
    """Extracts the default gateway from the adapter information."""
    match = re.search(r"Default Gateway[.\s]*: ([^\r\n]+)", adapter)
    if match:
        return match.group(1)
    return None


def main():
    """Checks for connected network adapters with IPv4 or IPv6 addresses and a default gateway assigned."""
    adapters = get_network_adapters()
    connected_adapters = []
    for adapter in re.split(r"\r\n\r\n", adapters):
        if has_default_gateway(adapter):
            if is_wifi(adapter):
                connected_adapters.append(("WiFi", adapter))
            elif is_ethernet(adapter):
                connected_adapters.append(("Ethernet", adapter))

    if connected_adapters:
        for adapter_type, adapter in connected_adapters:
            print("Connected adapter type: {}".format(adapter_type))
            ipv4_address = get_ipv4_address(adapter)
            ipv6_address = get_ipv6_address(adapter)
            default_gateway = get_default_gateway(adapter)
            print("IPv4 Address: {}".format(ipv4_address if ipv4_address else "Not available"))
            print("IPv6 Address: {}".format(ipv6_address if ipv6_address else "Not available"))
            print("Default Gateway: {}".format(default_gateway if default_gateway else "Not available"))
            print()
    else:
        print("No connected network adapters with IPv4 or IPv6 addresses and a default gateway assigned.")


if __name__ == "__main__":
    main()
