#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Win-10
#
# Created:     16/06/2019
# Copyright:   (c) Win-10 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------



#https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
#https://stackoverflow.com/questions/3718657/how-to-properly-determine-current-script-directory
#https://stackoverflow.com/questions/431684/how-do-i-change-directory-cd-in-python
#https://stackoverflow.com/questions/8248397/how-to-know-change-current-directory-in-python-shell
#https://stackoverflow.com/questions/431684/how-do-i-change-directory-cd-in-python
#https://stackoverflow.com/questions/tagged/working-directory

print("""
#https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
#https://stackoverflow.com/questions/3718657/how-to-properly-determine-current-script-directory
#https://stackoverflow.com/questions/431684/how-do-i-change-directory-cd-in-python
#https://stackoverflow.com/questions/8248397/how-to-know-change-current-directory-in-python-shell
#https://stackoverflow.com/questions/431684/how-do-i-change-directory-cd-in-python
#https://stackoverflow.com/questions/tagged/working-directory
""")
print("""To get the current working directory use
import os
print(os.getcwd())
""")

import os
print(os.getcwd())

print("# Prints the current working directory")
# Prints the current working directory
print("#To set the working directory:")
#To set the working directory:
print(os.chdir('G:/PyWorkDirectory'))
print("""
To # Provide the new path here
os.chdir('Python folder name or The desider directory name ')
""")
# Provide the new path here

file3 = open("G:/PyWorkDirectory/640px-Computer_system_bus.svg", "rb")
print(file3.read())
file3.close()


print(""" import os
cwd = os.getcwd()
print(cwd)
""")
import os
cwd = os.getcwd()
print(cwd)

#current answer is C:\Users\Win-10\AppData\Local\Temp

print("To get the current working directory use")
print("""
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
""")
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

print("""
(Note that the incantation above won't work if you've already used os.chdir()
 to change your current working directory, since the value of the __file__
 constant is relative to the current working directory and is not changed by
 an os.chdir() call.)
""")


print("""
You may find this useful as a reference:

import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))
""")


#You may find this useful as a reference:

import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

print("This file path, relative to os.getcwd()")
print(__file__ + "\n")

print("This file full path (following symlinks)")
full_path = os.path.realpath(__file__)
print(full_path + "\n")

print("This file directory and name")
path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

print("This file directory only")
print(os.path.dirname(full_path))


