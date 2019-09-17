#-------------------------------------------------------------------------------
# Name:        Writinginafile1
# Purpose:     Learn to Writing in a file
#
# Author:      Shyed Shahriar Housaini
#
# Created:     17/09/2019
# Copyright:   (c) Shyed Shahriar Housaini 2019
# Licence:     Terms from Shyed Shahriar Housaini
#-------------------------------------------------------------------------------


print(""" we can not write in a file which is open in a r read mode """)
print(""" if the file we are trying to write to by w , if that file does
not exist, that will be created, or if it does exist, with the same name,
 that file will be overwritten nad may get corrupted """)
with open("C:/ProgramFiles/Python37/2PAGLA2.txt", "w") as fl11:
    pass
print(""" with open("C:/ProgramFiles/Python37/2PAGLA2.txt", "w") as fl11:
    pass
that code block will only create the file """)

print(""" with open("C:/ProgramFiles/Python37/2PAGLA2.txt", "w") as fl11:
    fl11.write("rrrr")
that code block will create the file and write rrrr to it""")

with open("C:/ProgramFiles/Python37/2PAGLA2.txt", "w") as fl11:
    fl11.write("rr/nrrrr")
    fl11.write("RR\nRRRR")
    print(""""
    fl1.seek(o) start to write the file from begineening again""")
    fl11.seek(0)
    fl11.write("WW")
##    print("""" print (fl11.mode) tell us the mode of the file""")
##    print(fl11.mode)
##    print("""" print (fl11.tell()) tell us where we are now in the file""")
##    print (fl11.tell())
##    size_to_read = 10
##    f_content = fl11.read(size_to_read)
##
##    while len (f_content) > 0:
##        print (f_content, end='*')
##        print (fl11.tell())
##        f_content=fl11.read(size_to_read)
##
##
##print("""" /কি /কওরীন /আআই \আপওনীরা
##\ঊহাট \ইস \টহিস
##\ইহা \কি \? """)
