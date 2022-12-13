'''
Write an cross-platform program written in Python to get the OS info, and based on that OS info the code should give all the software and hardware info of computer based on different platforms and OS.
 Give platform-agnostic , windows and linux methods and codes to obtain hardware and software info
 
 
import platform

import importlib
importlib.reload(os)

import os
# Get the system name
system_name = platform.system()

# Get the system release
system_release = platform.release()

# Get the system version
system_version = platform.version()

# Get the machine type
machine = platform.machine()

# Get the processor name
processor = platform.processor()

# Get the total amount of physical memory
memory = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024. ** 3)

# Get the hostname
hostname = platform.node() 

# Print the system information
print("System name: " + system_name)
print("System release: " + system_release)
print("System version: " + system_version)
print("Machine type: " + machine)
print("Processor: " + processor)
print("Total memory: " + str(memory) + " GB")
print("Hostname: " + hostname) 

print("System name: ")
print("System release: ")
print("System version: ")
print("Machine type: ")
print("Processor: ")
print("Total memory: ")
print("Hostname: ") 

import platform

system_info = platform.uname()
'''
'''
print(f'System: {system_info.system}')
print(f'Node Name: {system_info.node}')
print(f'Release: {system_info.release}')
print(f'Version: {system_info.version}')
print(f'Machine: {system_info.machine}')
print(f'Processor: {system_info.processor}') '''

import platform

# Get hardware information
print("Hardware information:")
print("Operating System:", platform.system())
print("Machine:", platform.machine())
print("Processor:", platform.processor())

# Get software information
print("\nSoftware information:")
print("OS Name:", platform.system())
print("OS Version:", platform.release())
print("OS Architecture:", platform.architecture()[0])


'''
import platform

# Get the system's platform
system_platform = platform.system()

# Get the system's OS release
system_release = platform.release()

# Check the system's platform and use the appropriate method
# to obtain information about the system's hardware and software
if system_platform == "Linux":
    # Use Linux-specific methods to obtain hardware and software info
    pass
elif system_platform == "Windows":
    # Use Windows-specific methods to obtain hardware and software info
    pass
else:
    # Use platform-agnostic methods to obtain hardware and software info
    pass

# Print the obtained information
print("Platform: ", system_platform)
print("OS release: ", system_release)
print("Hardware: ", system_hardware)
print("Software: ", system_software)

'''

'''
To obtain hardware and software information on a computer using platform-agnostic methods, you can use the platform module in Python. This module provides various methods that can be used to obtain information about the system's hardware and software, regardless of the platform or operating system it is running on.

For example, the platform.machine() method returns the hardware information of the system, such as the processor architecture and the hardware model. The platform.uname() method returns a tuple containing information about the system's hardware and software, such as the system name, the release version, and the processor type.

To obtain hardware and software information on Windows systems, you can use the win32api module in Python. This module provides various methods that can be used to obtain information about the system's hardware and software, such as the processor type, the amount of memory installed, and the version of the operating system.

For example, the win32api.GetSystemInfo() method returns a tuple containing information about the system's hardware, such as the processor type, the number of processors, and the amount of memory installed. The win32api.GetVersionEx() method returns a tuple containing information about the system's software, such as the version of the operating system and the type of the operating system.

To obtain hardware and software information on Linux systems, you can use the psutil module in Python. This module provides various methods that can be used to obtain information about the system's hardware and software, such as the processor type, the amount of memory installed, and the version of the operating system.
'''

import os
def get_os_info():
    return platform.system()

def get_hardware_info():
  # Use the `uname` command to get hardware info on Linux
  if get_os_info() == "Linux":
    return os.uname()
  # Use the `systeminfo` command to get hardware info on Windows
  elif get_os_info() == "Windows":
    return os.popen("systeminfo").read()

def get_software_info():
  # Use the `dpkg` command to get installed software on Linux
  if get_os_info() == "Linux":
    return os.popen("dpkg -l").read()
  # Use the `wmic` command to get installed software on Windows
  elif get_os_info() == "Windows":
    return os.popen("wmic product get name, version").read()
  
  
  
print("System name: ")
print("System release: ")
print("System version: ")
print("Machine type: ")
print("Processor: ")
print("Total memory: ")
print("Hostname: ") 