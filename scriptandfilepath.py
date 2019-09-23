#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shyed Shahriar Housaini
#
# Created:     20/09/2019
# Copyright:   (c) Shyed Shahriar Housaini 2019
# Licence:     <your licence, "Shyed Shahriar Housaini Terms and Conditions">
#-------------------------------------------------------------------------------
import os
print(os.getcwd)
print(os.getcwd())
File11 = open("G:/PyWorkDirectory/newfile.txt", "w")
File11.write('''Line 1 This has been written to a file
Line 2 This has been written to a file
Line 3 This has been written to a file
Line 4 This has been written to a file
Line 5 This has been written to a file
Line 6 This has been written to a file
Line 7 This has been written to a file''')
File11.close()

File12 = open("G:/PyWorkDirectory/newfile.txt", "r")
print(File12.read())
File12.close()

dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
scriptpath = os.path.realpath(__file__)
print("Script path is : " + scriptpath)


print("print the name of the file by  print(fl.name)")
print(File12.name)
print("print the mode the file is opened in by print(fl.mode) ")
print(File12.mode)
