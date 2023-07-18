import json
import subprocess

def parse_network_config(text):
    network_config = {}
    current_adapter = None

    for line in text.splitlines():
        if line.strip() != "":
            if line.startswith("   "):
                # If the line starts with three spaces, it contains adapter configuration details
                if current_adapter:
                    # Split the line by the first occurrence of ':' and remove leading/trailing spaces
                    key, value = map(str.strip, line.split(':', 1))
                    network_config[current_adapter][key] = value
            else:
                # If the line doesn't start with three spaces, it is a new adapter name
                adapter_name = line.split(':', 1)[0].strip()
                network_config[adapter_name] = {}
                current_adapter = adapter_name
    return network_config

def write_to_txt(data, filename):
    # Write data to a text file in JSON format
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data))

def read_from_txt(filename):
    # Read data from a text file in JSON format
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_to_json(data, filename):
    # Write data to a JSON file with proper formatting
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def main():
    # Execute the 'ipconfig /all' command and capture the output
    process = subprocess.Popen(
        "ipconfig /all",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output, _ = process.communicate()

    # Convert the output to a string
    network_config_text = output.decode('utf-8')

    # Parse the network configuration from the text
    network_config_data = parse_network_config(network_config_text)

    # Write the network configuration to a text file
    write_to_txt(network_config_data, 'AUTOnetwork_config.txt')

    # Read the network configuration from the text file
    read_data = read_from_txt('AUTOnetwork_config.txt')

    # Get the names of adapters connected to the internet
    internet_connected_adapters = [
        adapter_name
        for adapter_name, config in read_data.items()
        if config.get('Default Gateway') != ''
    ]

    print("Internet connected adapters:")
    for adapter_name in internet_connected_adapters:
        print(adapter_name)

    # Write the network configuration to a JSON file
    write_to_json(read_data, 'AUTOnetwork_config.json')

if __name__ == '__main__':
    main()
