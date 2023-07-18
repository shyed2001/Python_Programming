import json

def parse_network_config(text):
    # Create an empty dictionary to store the network configuration
    network_config = {}
    
    # Initialize the current adapter variable
    current_adapter = None

    # Split the text into individual lines
    for line in text.splitlines():
        # Check if the line is not empty
        if line.strip() != "":
            # Check if the line starts with multiple spaces indicating adapter details
            if line.startswith("   "):
                # Check if there is a current adapter being processed
                if current_adapter:
                    # Split the line into key and value using ":" as the separator
                    key, value = map(str.strip, line.split(':', 1))
                    # Add the key-value pair to the current adapter in the network configuration
                    network_config[current_adapter][key] = value
            else:
                # Split the line into adapter name and discard the rest of the line
                adapter_name = line.split(':', 1)[0].strip()
                # Create a new dictionary for the adapter in the network configuration
                network_config[adapter_name] = {}
                # Set the current adapter to the current adapter name
                current_adapter = adapter_name

    # Return the network configuration dictionary
    return network_config


def write_to_txt(data, filename):
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write the JSON representation of the data to the file
        file.write(json.dumps(data))

def read_from_txt(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Load the JSON data from the file and return it
        return json.load(file)

def write_to_json(data, filename):
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write the JSON representation of the data to the file with indentation
        json.dump(data, file, indent=4)

# The provided network configuration text
network_config_text = """
Windows IP Configuration

   Host Name . . . . . . . . . . . . : DESKTOP-LSNQ60O
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No

Ethernet adapter vEthernet (WiFi):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter
   Physical Address. . . . . . . . . : 00-15-5D-4B-D5-D4
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::e3db:8adc:b5ba:f86a%43(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.27.64.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 721425757
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter vEthernet (Default Switch):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter #2
   Physical Address. . . . . . . . . : 00-15-5D-4D-04-D0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::be91:8b1f:bd17:d231%48(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.20.80.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 805311837
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter vEthernet (Ethernet):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter #3
   Physical Address. . . . . . . . . : 00-15-5D-81-7D-88
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::2dc7:744:315c:8f9b%53(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.30.32.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 889197917
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter vEthernet (WSL):

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Hyper-V Virtual Ethernet Adapter #7
   Physical Address. . . . . . . . . : 00-15-5D-4C-2D-49
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::3719:be38:3907:fdc0%75(Preferred)
   IPv4 Address. . . . . . . . . . . : 172.29.64.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.240.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 1258296669
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter Ethernet 2:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter
   Physical Address. . . . . . . . . : 0A-00-27-00-00-10
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::fd76:63cf:a03a:8329%16(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.56.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :
   DHCPv6 IAID . . . . . . . . . . . : 1208614951
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   NetBIOS over Tcpip. . . . . . . . : Enabled

Wireless LAN adapter Local Area Connection* 1:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   Physical Address. . . . . . . . . : F8-AC-65-AF-6A-55
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Local Area Connection* 10:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #2
   Physical Address. . . . . . . . . : FA-AC-65-AF-6A-54
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Realtek PCIe GbE Family Controller
   Physical Address. . . . . . . . . : C0-3E-BA-2F-DC-95
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::deaa:d774:ac1a:7ca7%4(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.1.114(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Sunday, July 16, 2023 7:38:28 PM
   Lease Expires . . . . . . . . . . : Monday, July 17, 2023 4:06:02 AM
   Default Gateway . . . . . . . . . : 192.168.1.1
   DHCP Server . . . . . . . . . . . : 192.168.1.1
   DHCPv6 IAID . . . . . . . . . . . : 79707834
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   DNS Servers . . . . . . . . . . . : 192.168.1.1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter VMware Network Adapter VMnet1:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VMware Virtual Ethernet Adapter for VMnet1
   Physical Address. . . . . . . . . : 00-50-56-C0-00-01
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::1122:75c1:6faa:ad02%7(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.64.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Sunday, July 16, 2023 7:38:14 PM
   Lease Expires . . . . . . . . . . : Monday, July 17, 2023 2:38:13 AM
   Default Gateway . . . . . . . . . :
   DHCP Server . . . . . . . . . . . : 192.168.64.254
   DHCPv6 IAID . . . . . . . . . . . : 838881366
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter VMware Network Adapter VMnet8:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : VMware Virtual Ethernet Adapter for VMnet8
   Physical Address. . . . . . . . . : 00-50-56-C0-00-08
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::dea8:74d3:f731:e772%14(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.209.1(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Sunday, July 16, 2023 7:38:14 PM
   Lease Expires . . . . . . . . . . : Monday, July 17, 2023 2:38:13 AM
   Default Gateway . . . . . . . . . :
   DHCP Server . . . . . . . . . . . : 192.168.209.254
   DHCPv6 IAID . . . . . . . . . . . : 855658582
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   Primary WINS Server . . . . . . . : 192.168.209.2
   NetBIOS over Tcpip. . . . . . . . : Enabled

Wireless LAN adapter WiFi:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) Wireless-AC 9560
   Physical Address. . . . . . . . . : F8-AC-65-AF-6A-54
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::2f3:558:166c:79a1%2(Preferred)
   IPv4 Address. . . . . . . . . . . : 192.168.1.112(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Sunday, July 16, 2023 7:38:14 PM
   Lease Expires . . . . . . . . . . : Monday, July 17, 2023 4:06:03 AM
   Default Gateway . . . . . . . . . : 192.168.1.1
   DHCP Server . . . . . . . . . . . : 192.168.1.1
   DHCPv6 IAID . . . . . . . . . . . : 128006122
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2A-35-FF-02-C0-3E-BA-2F-DC-95
   DNS Servers . . . . . . . . . . . : 192.168.1.1
                                       8.8.8.8
   NetBIOS over Tcpip. . . . . . . . : Enabled
"""

# Parse the network configuration text
network_config = parse_network_config(network_config_text)

# Write the parsed network configuration to a JSON file
write_to_json(network_config, 'network_config.json')

# Read the network configuration from the JSON file
network_config_from_file = read_from_txt('network_config.json')

# Print the network configuration
print(network_config_from_file)



"""
   Here are explanations of various steps in the code:

The parse_network_config function takes a text parameter, which represents the network configuration text.

The function creates an empty dictionary called network_config to store the network configuration.

The current_adapter variable is initialized to None. It will be used to keep track of the current adapter being processed.

The text parameter is split into individual lines using the splitlines() method.

The code iterates over each line in the text using a for loop.

The if line.strip() != "": condition checks if the line is not empty. The strip() method is used to remove leading and trailing whitespaces.

If the line starts with multiple spaces, it indicates adapter details.

The if line.startswith(" "): condition checks if the line starts with three spaces.

If there is a current adapter being processed, the code enters the nested if statement.

The line is split into key-value pairs using the split(':', 1) method. The 1 argument in split(':', 1) limits the split to the first occurrence of ':'.

The map(str.strip, line.split(':', 1)) function applies the str.strip method to remove leading and trailing whitespaces from the key and value.

The key and value variables store the split key-value pair.

The key-value pair is added to the network_config dictionary under the current adapter.

If the line doesn't start with three spaces, it indicates a new adapter.

The line is split at the first occurrence of ':' using the split(':', 1) method.

The adapter_name variable stores the adapter name obtained from the split line.

A new dictionary is created for the adapter in the network_config dictionary.

The current adapter variable is updated to the new adapter name.

After processing all lines, the function returns the network_config dictionary containing the parsed network configuration.

The write_to_txt function takes two parameters: data and filename.

The function opens the specified file in write mode using the open(filename, 'w') statement. The file object is automatically closed when the with block is exited.

The json.dumps function is used to convert the data to a JSON-formatted string.

The JSON-formatted string is written to the file using the write method of the file object.

The read_from_txt function takes a filename parameter.

The function opens the specified file in read mode using the open(filename, 'r') statement. The file object is automatically closed when the with block is exited.

The json.load function is used to load the JSON-formatted data from the file.

The loaded JSON data is returned from the function.

The write_to_json function takes two parameters: data and filename.

The function opens the specified file in write mode using the open(filename, 'w') statement. The file object is automatically closed when the with block is exited.

The json.dump function is used to write the data to the file in JSON format with indentation for readability.

The get_ipconfig_results function retrieves the results of the ipconfig /all command and returns the JSON-formatted output.

The function creates a temporary file using the tempfile.NamedTemporaryFile() context manager.

The subprocess.run function is used to run the ipconfig /all command and redirect the output to the temporary file.

The file pointer is rewound to the beginning using the seek(0) method.

The content of the temporary file is read using the read() method and decoded as a UTF-8 string.

The re.split function is used to split the output into individual adapter sections using the regex pattern \r\n\r\n.

The function initializes an empty list called result to store the parsed adapter information.

The code iterates over each adapter in the adapters list using a for loop.

Inside the loop, a dictionary called adapter_info is created to store the information of the current adapter.

The re.search function is used to extract specific information from the adapter section using regex patterns.

If the regex pattern matches a description, the description is stored in the adapter_info dictionary under the key "Description".

If the regex pattern matches an IPv4 address, the address is stored in the adapter_info dictionary under the key "IPv4 Address".

If the regex pattern matches an IPv6 address, the address is stored in the adapter_info dictionary under the key "IPv6 Address".

If the regex pattern matches a default gateway, the gateway is stored in the adapter_info dictionary under the key "Default Gateway".

If the adapter_info dictionary contains any information, it is appended to the result list.

After processing all adapters, the result list is returned from the function.

The main function serves as the entry point of the program.

The get_ipconfig_results function is called to retrieve the ipconfig results.

If the results list is not empty, the program proceeds to write the results to a JSON file.

The open function is used to open the file "ipconfig.json" in write mode.

The json.dump function is used to write the results to the file in JSON format with indentation for readability.

A success message is printed if the file creation is successful.

If the results list is empty, a failure message is printed.

The if __name__ == "__main__": condition ensures that the main function is only executed when the script is run directly (not imported as a module).

The main function is called to start the program execution.

Here are explanations of various steps in the code:

The parse_network_config function takes a text parameter, which represents the network configuration text.

The function creates an empty dictionary called network_config to store the network configuration.

The current_adapter variable is initialized to None. It will be used to keep track of the current adapter being processed.

The text parameter is split into individual lines using the splitlines() method.

The code iterates over each line in the text using a for loop.

The if line.strip() != "": condition checks if the line is not empty. The strip() method is used to remove leading and trailing whitespaces.

If the line starts with multiple spaces, it indicates adapter details.

The if line.startswith(" "): condition checks if the line starts with three spaces.

If there is a current adapter being processed, the code enters the nested if statement.

The line is split into key-value pairs using the split(':', 1) method. The 1 argument in split(':', 1) limits the split to the first occurrence of ':'.

The map(str.strip, line.split(':', 1)) function applies the str.strip method to remove leading and trailing whitespaces from the key and value.

The key and value variables store the split key-value pair.

The key-value pair is added to the network_config dictionary under the current adapter.

If the line doesn't start with three spaces, it indicates a new adapter.

The line is split at the first occurrence of ':' using the split(':', 1) method.

The adapter_name variable stores the adapter name obtained from the split line.

A new dictionary is created for the adapter in the network_config dictionary.

The current adapter variable is updated to the new adapter name.

After processing all lines, the function returns the network_config dictionary containing the parsed network configuration.

The write_to_txt function takes two parameters: data and filename.

The function opens the specified file in write mode using the open(filename, 'w') statement. The file object is automatically closed when the with block is exited.

The json.dumps function is used to convert the data to a JSON-formatted string.

The JSON-formatted string is written to the file using the write method of the file object.

The read_from_txt function takes a filename parameter.

The function opens the specified file in read mode using the open(filename, 'r') statement. The file object is automatically closed when the with block is exited.

The json.load function is used to load the JSON-formatted data from the file.

The loaded JSON data is returned from the function.

The write_to_json function takes two parameters: data and filename.

The function opens the specified file in write mode using the open(filename, 'w') statement. The file object is automatically closed when the with block is exited.

The json.dump function is used to write the data to the file in JSON format with indentation for readability.

The get_ipconfig_results function retrieves the results of the ipconfig /all command and returns the JSON-formatted output.

The function creates a temporary file using the tempfile.NamedTemporaryFile() context manager.

The subprocess.run function is used to run the ipconfig /all command and redirect the output to the temporary file.

The file pointer is rewound to the beginning using the seek(0) method.

The content of the temporary file is read using the read() method and decoded as a UTF-8 string.

The re.split function is used to split the output into individual adapter sections using the regex pattern \r\n\r\n.

The function initializes an empty list called result to store the parsed adapter information.

The code iterates over each adapter in the adapters list using a for loop.

Inside the loop, a dictionary called adapter_info is created to store the information of the current adapter.

The re.search function is used to extract specific information from the adapter section using regex patterns.

If the regex pattern matches a description, the description is stored in the adapter_info dictionary under the key "Description".

If the regex pattern matches an IPv4 address, the address is stored in the adapter_info dictionary under the key "IPv4 Address".

If the regex pattern matches an IPv6 address, the address is stored in the adapter_info dictionary under the key "IPv6 Address".

If the regex pattern matches a default gateway, the gateway is stored in the adapter_info dictionary under the key "Default Gateway".

If the adapter_info dictionary contains any information, it is appended to the result list.

After processing all adapters, the result list is returned from the function.

The main function serves as the entry point of the program.

The get_ipconfig_results function is called to retrieve the ipconfig results.

If the results list is not empty, the program proceeds to write the results to a JSON file.

The open function is used to open the file "ipconfig.json" in write mode.

The json.dump function is used to write the results to the file in JSON format with indentation for readability.

A success message is printed if the file creation is successful.

If the results list is empty, a failure message is printed.

The if __name__ == "__main__": condition ensures that the main function is only executed when the script is run directly (not imported as a module).

The main function is called to start the program execution.
   """