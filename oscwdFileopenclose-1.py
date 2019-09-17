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
fl = open("C:/ProgramFiles/Python37/TEST111.txt", "r+")
print("print the name of the file by  print(fl.name)")
print(fl.name)
print("print the mode the file is opened in by print(fl.mode) ")
print(fl.mode)

print(fl.read())
fl.close

print(""" Reading file bit by bit """)

fl1 = open("C:/ProgramFiles/Python37/pagla.txt", "r+")
print("print the name of the file by  print(fl1.name)")
print(fl1.name)
print("print the mode the file is opened in by print(fl1.mode) ")
print(fl1.mode)
print("to read bit by bit we can use 'print(fl1.read(0))' ")
print(fl1.read(0))
print(fl1.read(1))
print("""" fl1.seek(0) starts reading from zero pisition of the file""")
fl1.seek(0)
print(fl1.read(2))
print(fl1.read(3))
print(fl1.read(4))
print("""" fl1.seek(0) starts reading from zero pisition of the file""")
fl1.seek(0)
print(fl1.read(5))
print(fl1.read(7))
print(fl1.read(9))
fl1.close

print(""" Reading file line by line """)
fl1 = open("C:/ProgramFiles/Python37/pagla.txt", "r+")
print("print the name of the file by  print(fl1.name)")
print(fl1.name)
print("print the mode the file is opened in by print(fl1.mode) ")
print(fl1.mode)
print("""to read line by line we can use one or many
'print(fl1.readline())' for each desired line """)
print(fl1.readline())
print(fl1.readline())
print(fl1.readline(7))
print("""to read all the content as a list we can use
'print(fl1.readlines())' for all desired line """)
print(fl1.readlines())
fl1.close
print(""" the above readlines code will show list items
 starting from 3, because there were 3 lines 0, 1, 2 were
 already read after the file had been opened """)
print(""" also can open file by code block -
"with open("pagla.txt", "r+") as fl1:
    pass"
that was a content manager. the program will autometically close the file
 when outside the nblock and if there is any error, the code will exit
  and thus close the file, so the file will not be corrupted
 """)
with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl1:
    pass
print(""" also can read content of file by code block -
with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl1:
    fl1_content= fl1.read()
    print(fl1_content)
 """)
with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl1:
    fl1_content= fl1.read()
    print(fl1_content)
print(""" also can read content of file in list form by code block -
with open("pagla.txt", "r+") as fl1:
    fl1_contentlines= fl1.readlines()
    print(fl1_contentlines)
 """)
with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl1:
    fl1_contentlines= fl1.readlines()
    print(fl1_contentlines)
print(""" also can read one line at a time form the file by code block,
(here shown for two lines) -
with open("pagla.txt", "r+") as fl1:
    fl1_contentperline= fl1.readline()
    print(fl1_contentperline)
    fl1_contentperline= fl1.readline()
    print(fl1_contentperline)
 """)
print(""" put end='' after every print line statement to
  stop the auto newline after each line is printed
 """)
with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl1:
    fl1_contentperline= fl1.readline()
    print(fl1_contentperline)
    print(fl1_content)
    print("""" print (fl1.mode) tell us the mode of the file""")
    print(fl1.mode)
    print("""" print (fl1.tell()) tell us where we are now in the file""")
    fl1_contentperline= fl1.readline()
    print(fl1_contentperline)


with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl1:
    fl1_contentperline= fl1.readline()
    print(fl1_contentperline,end='')

    fl1_contentperline= fl1.readline()
    print(fl1_contentperline, end='')
    print("""" fl1.seek(0) starts reading from zero pisition of the file""")
    fl1.seek(0)
    fl1_contentperline= fl1.readline()
    print(fl1_contentperline, end='')

print(""" also can read content 75 BIT at once in this case of file by
code block -
with open("pagla.txt", "r+") as fl1:
    fl1_content= fl1.read()
    print(fl1_content)
if there is no bits left in the the file as specified in program script, the
program will print empty script """)

with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl1:
    fl1_content= fl1.read(75)
    print(fl1_content)
    print("""" print (fl1.mode) tell us the mode of the file""")
    print(fl1.mode)
    print("""" print (fl1.tell()) tell us where we are now in the file""")
    print (fl1.tell())
    print("""" fl1.seek(0) starts reading from zero pisition of the file""")
    fl1.seek(0)
    fl1_content= fl1.read(75)
    print(fl1_content)

    fl1_content= fl1.read(75)
    print(fl1_content)
print(""" also can read content by for loop in this case of file by
code block -
with open("pagla.txt", "r+") as fl1:
    for line in fl11:
        print (line, end='')
 this will save us from running out of memory at once while trying to
  read a very large file at once """)

with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl11:
    print(fl11.mode)
    for line in fl11:
        print (line, end='')



print(""" also can read content by 'with' and 'while' loop in this case of
file by code block -
with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl11:

    size_to_read = 10
    f_content = fl11.read(size_to_read)

    while len (f_content) > 0:
        print (f_content, end='*')
        f_content=fl11.read(size_to_read)

reading the whole file  10 bits at a time.  """)
with open("C:/ProgramFiles/Python37/pagla.txt", "r+") as fl11:
    print("""" print (fl11.mode) tell us the mode of the file""")
    print(fl11.mode)
    print("""" print (fl11.tell()) tell us where we are now in the file""")
    print (fl11.tell())
    size_to_read = 10
    f_content = fl11.read(size_to_read)

    while len (f_content) > 0:
        print (f_content, end='*')
        print (fl11.tell())
        f_content=fl11.read(size_to_read)


print("""" /কি /কওরীন /আআই \আপওনীরা
\ঊহাট \ইস \টহিস
\ইহা \কি \? """)