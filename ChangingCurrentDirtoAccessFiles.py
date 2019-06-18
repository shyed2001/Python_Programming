#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Win-10
#
# Created:     16/06/2019
# Copyright:   (c) Win-10 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

print("""
import os

print(os.getcwd())

os.chdir('G:/PyWorkDirectory' )

print(os.getcwd())


file = open("C:/Program Files/Python373/forloop.txt", "r")
print(file.read(16))
print(161616161616161616161616161611616161616161)
print(file.read(4))
print(1414141414141414141414141414414141414414141414141441144141)
print(file.read(4))
print(2424242424242424242424242424242424242424242424)
print(file.read())
file.close()



file2 = open("G:/PyWorkDirectory/filename.txt", "r")
print(file2.read(16))
print(161616161616161616161616161611616161616161)
print(file2.read(4))
print(1414141414141414141414141414414141414414141414141441144141)
print(file2.read(4))
print(2424242424242424242424242424242424242424242424)
print(file2.read())
file2.close()
""")
import os

print(os.getcwd())

os.chdir('G:/PyWorkDirectory' )

print(os.getcwd())


file = open("C:/Program Files/Python373/forloop.txt", "r")
print(file.read(16))
print(161616161616161616161616161611616161616161)
print(file.read(4))
print(1414141414141414141414141414414141414414141414141441144141)
print(file.read(4))
print(2424242424242424242424242424242424242424242424)
print(file.read())
file.close()



file2 = open("filename.txt", "r")
print(file2.read(16))
print(161616161616161616161616161611616161616161)
print(file2.read(4))
print(1414141414141414141414141414414141414414141414141441144141)
print(file2.read(4))
print(2424242424242424242424242424242424242424242424)
print(file2.read())
file2.close()

