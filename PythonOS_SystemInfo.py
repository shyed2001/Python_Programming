""" import platform

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
hostname = platform.node() """

# Print the system information
""" print("System name: " + system_name)
print("System release: " + system_release)
print("System version: " + system_version)
print("Machine type: " + machine)
print("Processor: " + processor)
print("Total memory: " + str(memory) + " GB")
print("Hostname: " + hostname) """

print("System name: ")
print("System release: ")
print("System version: ")
print("Machine type: ")
print("Processor: ")
print("Total memory: ")
print("Hostname: ")