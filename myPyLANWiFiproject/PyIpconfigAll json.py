import json
import re
import tempfile
import subprocess

def get_ipconfig_results():
    """Gets the results of ipconfig /all and returns the JSON-formatted output."""

    # Create a temporary file to store the ipconfig output
    with tempfile.NamedTemporaryFile() as f:
        # Run the ipconfig /all command and redirect the output to the temporary file
        subprocess.run(["ipconfig", "/all"], stdout=f)
        
        # Rewind the file pointer to the beginning
        f.seek(0)
        
        # Read the ipconfig output from the temporary file
        ipconfig_output = f.read().decode("utf-8")
        
        # Split the output into individual adapter sections
        adapters = re.split(r"\r\n\r\n", ipconfig_output)
        result = []
        
        for adapter in adapters:
            adapter_info = {}
            
            # Extract the adapter description using regex
            description = re.search(r"Description[.\s]*: ([^\r\n]+)", adapter)
            if description:
                # Store the adapter description in the adapter_info dictionary
                adapter_info["Description"] = description.group(1)
            
            # Extract the IPv4 address using regex
            ipv4_address = re.search(r"IPv4 Address[.\s]*: ([^\r\n]+)", adapter)
            if ipv4_address:
                # Store the IPv4 address in the adapter_info dictionary
                adapter_info["IPv4 Address"] = ipv4_address.group(1)
            
            # Extract the IPv6 address using regex
            ipv6_address = re.search(r"IPv6 Address[.\s]*: ([^\r\n]+)", adapter)
            if ipv6_address:
                # Store the IPv6 address in the adapter_info dictionary
                adapter_info["IPv6 Address"] = ipv6_address.group(1)
            
            # Extract the default gateway using regex
            default_gateway = re.search(r"Default Gateway[.\s]*: ([^\r\n]+)", adapter)
            if default_gateway:
                # Store the default gateway in the adapter_info dictionary
                adapter_info["Default Gateway"] = default_gateway.group(1)
            
            # Add the adapter info to the result list if it contains any information
            if adapter_info:
                result.append(adapter_info)
        
        return result

def main():
    # Retrieve the ipconfig results
    results = get_ipconfig_results()
    
    if results:
        # Write the results to a JSON file
        with open("ipconfig.json", "w") as f:
            json.dump(results, f, indent=4)
            print("ipconfig.json file created.")
    else:
        print("Failed to retrieve ipconfig results.")

if __name__ == "__main__":
    main()


# This code retrieves the results of the ipconfig /all command and stores them in a JSON file. Here's an explanation of each part:

# The get_ipconfig_results function retrieves the output of the ipconfig /all command and returns it in JSON format. It uses a temporary file to capture the command output.

# Within the function, a temporary file is created using tempfile.NamedTemporaryFile(). It automatically handles the creation and deletion of the temporary file.

# The subprocess.run function runs the ipconfig /all command and redirects the output to the temporary file using stdout=f.

# The file pointer is rewound to the beginning using f.seek(0) so that the content can be read from the start.

# The content of the temporary file is read using f.read().decode("utf-8"). It is decoded from bytes to a string using the UTF-8 encoding.

# The ipconfig output is split into individual adapter sections using re.split(r"\r\n\r\n", ipconfig_output). Each adapter section represents information about a network adapter.

# Within the loop, adapter information is extracted using regular expressions. The description, IPv4 address, IPv6 address, and default gateway are matched using regex patterns and stored in the adapter_info dictionary.

# If the adapter_info dictionary contains any information, it is appended to the result list.

# The function returns the result list, which contains dictionaries representing the network adapter information.

# The main function is responsible for calling get_ipconfig_results and writing the results to a JSON file.

# In the main function, the get_ipconfig_results function is called to retrieve the network adapter information.

# If the results list is not empty, the information is written to a JSON file named "ipconfig.json" using json.dump. The indent=4 argument is used to add indentation for readability.

# If the results list is empty, a message is printed indicating that the retrieval of ipconfig results failed.

# This code assumes that you have the necessary permissions to run the ipconfig command and read/write files on your system.