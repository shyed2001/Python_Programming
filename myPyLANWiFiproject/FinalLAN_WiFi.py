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


# In this code, we have a few functions to parse, write, and read network configuration data. Here's an explanation of each part:

# The parse_network_config function takes the network configuration text as input and returns a dictionary containing the parsed network configuration. It iterates over each line of the text, checks if it represents a property of the current adapter or a new adapter, and stores the properties accordingly in the dictionary.

# The write_to_txt function writes the network configuration data to a TXT file. It opens the specified file in write mode and converts the data to a JSON-formatted string using json.dumps(). The resulting string is then written to the file.

# The read_from_txt function reads the network configuration data from a TXT file. It opens the specified file in read mode and uses json.load() to load the JSON-formatted data from the file. The loaded data is then returned.

# The write_to_json function writes the network configuration data to a JSON file. It opens the specified file in write mode and uses json.dump() to write the data in JSON format with indentation for readability.

# The code uses the subprocess module to execute the "ipconfig /all" command and captures its output. The Popen function is used to start the process, and communicate() is called to capture the stdout and stderr outputs.

# The command output is decoded from bytes to a string using output.decode('utf-8'), assuming the output is in UTF-8 encoding.

# The parse_network_config function is called with the network configuration text to obtain a parsed dictionary representation of the network configuration.

# The write_to_txt function is used to write the parsed network configuration data to a TXT file.

# The read_from_txt function is used to read the data back from the TXT file into the read_data variable.

# Finally, the write_to_json function is used to write the read_data to a JSON file with indentation.

# Please note that this code assumes you have the necessary permissions to execute the "ipconfig" command and read/write files on your system. Also, ensure that the file paths provided for reading and writing exist and are accessible.