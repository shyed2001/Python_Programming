print("""Must run the IDE or text editor as adminstrator
 to run/edit/save this program/script as/if these files are in C drive
  of the computer""")

import os

dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)

import os

dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
scriptpath = os.path.realpath(__file__)
print("Script path is : " + scriptpath)

print(""" Reading file all at once """)
fl = open("TEST111.txt", "r+")
print("print the name of the file by  print(fl.name)")
print(fl.name)
print("print the mode the file is opened in by print(fl.mode) ")
print(fl.mode)

print(fl.read())
fl.close

print(""" Reading file bit by bit """)

fl1 = open("pagla.txt", "r+")
print("print the name of the file by  print(fl1.name)")
print(fl1.name)
print("print the mode the file is opened in by print(fl1.mode) ")
print(fl1.mode)
print(fl1.read(0))
print(fl1.read(1))
print(fl1.read(2))
print(fl1.read(3))
print(fl1.read(4))
print(fl1.read(5))
print(fl1.read(7))
print(fl1.read(9))
fl1.close

print(""" Reading file line by line """)
fl1 = open("pagla.txt", "r+")
print("print the name of the file by  print(fl1.name)")
print(fl1.name)
print("print the mode the file is opened in by print(fl1.mode) ")
print(fl1.mode)
print(fl1.readline())
print(fl1.readline())
print(fl1.readline(7))
fl1.close

print(""" also cxan open file by code block -
"with open("pagla.txt", "r+") as fl1:
    pass"
the program will autometically close the file when outside
 the nblock and if there is any error, the code will exit
  and thus close the file, so the file will not be corrupted
 """)
with open("pagla.txt", "r+") as fl1:
    pass

print("""\nকি কওরীন আআই আপওনীরা
ঊহাট ইস টহিস
ইহা কি ? """)
