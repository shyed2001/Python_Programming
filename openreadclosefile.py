#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Win-10
#
# Created:     16/09/2019
# Copyright:   (c) Win-10 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

print(os.getcwd())


PPyfile=open("C:/Users/Win-10/AppData/Local/Temp/PyListstemp.txt", "r")
PPyfile1=open("C:/Users/Win-10/AppData/Local/Temp/PyForLoopstemp.txt", "r")
PPyfile4=open("C:/Users/Win-10/AppData/Local/Temp/NewTextDocumenttemp.txt")

print(PPyfile.read())
print(PPyfile1.read())
print(PPyfile4.read())


PPyfile2=open("G:/PyWorkDirectory/PyListstest.txt", "r")
PPyfile3=open("G:/PyWorkDirectory/PyForLoopstest.txt", "r")
PPyfile5=open("G:/PyWorkDirectory/NewTextDocumenttest.txt")

print("# Prints the current working directory")
# Prints the current working directory
print("#To set the working directory:")
#To set the working directory:
print(os.chdir('G:/PyWorkDirectory'))
print("""
To # Provide the new path here
os.chdir('Python folder name or The desider directory name ')
""")

print(os.getcwd())

print(PPyfile2.read())
print(PPyfile3.read())
print(PPyfile5.read())

PPyfile.close()
PPyfile1.close()
PPyfile2.close()
PPyfile3.close()
PPyfile4.close()
PPyfile5.close()
