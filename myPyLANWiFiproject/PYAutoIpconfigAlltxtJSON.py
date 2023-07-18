import json
import subprocess

def parse_network_config(text):
    # Initialize an empty dictionary to store the network configuration
    network_config = {}
    
    # Variable to keep track of the current adapter being processed
    current_adapter = None

    # Iterate over each line in the provided text
    for line in text.splitlines():
        # Check if the line is not empty
        if line.strip() != "":
            # Check if the line starts with "   ", indicating a property of the current adapter
            if line.startswith("   "):
                # Check if there is a current adapter being processed
                if current_adapter:
                    # Split the line into key-value pair by the first occurrence of ':'
                    key, value = map(str.strip, line.split(':', 1))
                    
                    # Store the property in the network configuration dictionary under the current adapter
                    network_config[current_adapter][key] = value
            else:
                # The line represents a new adapter
                
                # Extract the adapter name by splitting the line at the first occurrence of ':'
                adapter_name = line.split(':', 1)[0].strip()
                
                # Initialize an empty dictionary for the properties of the new adapter
                network_config[adapter_name] = {}
                
                # Update the current adapter variable
                current_adapter = adapter_name

    # Return the parsed network configuration
    return network_config


def write_to_txt(data, filename):
    # Open the specified file in write mode
    with open(filename, 'w') as file:
        # Convert the data to a JSON-formatted string and write it to the file
        file.write(json.dumps(data))

def read_from_txt(filename):
    # Open the specified file in read mode
    with open(filename, 'r') as file:
        # Load the JSON-formatted data from the file and return it
        return json.load(file)

def write_to_json(data, filename):
    # Open the specified file in write mode
    with open(filename, 'w') as file:
        # Write the data to the file in JSON format with indentation for readability
        json.dump(data, file, indent=4)

# Execute the "ipconfig /all" command and capture its output
process = subprocess.Popen("ipconfig /all", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, _ = process.communicate()

# Convert the command output to a string
network_config_text = output.decode('utf-8')

# Parse the network configuration data
network_config_data = parse_network_config(network_config_text)

# Write the data to a TXT file
write_to_txt(network_config_data, 'AUTOnetwork_config.txt')

# Read the data from the TXT file
read_data = read_from_txt('network_config.txt')

# Write the data to a JSON file
write_to_json(read_data, 'AUTOnetwork_config.json')


# This code performs the following steps:

# It defines a function parse_network_config that takes the network configuration text as input and returns a parsed dictionary representation of the network configuration.
# It defines three utility functions: write_to_txt, read_from_txt, and write_to_json to write and read the network configuration data to and from files in TXT and JSON formats.
# It uses the subprocess module to execute the ipconfig /all command and capture its output.
# The output of the command is then converted to a string.
# The parse_network_config function is called with the network configuration text to obtain a parsed dictionary representation of the network configuration.
# The parsed network configuration data is written to a TXT file using the write_to_txt function.
# The data is then read back from the TXT file using the read_from_txt function.
# Finally, the data is written to a JSON file with indentation using the write_to_json function.
# Please note that this code assumes that you have the required permissions to execute the ipconfig command and read/write files on your system. Also, ensure that the file paths provided for reading and writing exist and are accessible.