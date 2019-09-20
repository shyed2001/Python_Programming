#-------------------------------------------------------------------------------
# Name:        G:\PyWorkDirectory\makefileobjectbyiostringIO.py
# Purpose:      Practice
#
# Author:      Shyed Shahriar Housaini
#
# Created:     19/09/2019
# Copyright:   (c) Shyed Shahriar Housaini
# Licence:     Terms by Shyed Shahriar Housaini
#-------------------------------------------------------------------------------


#If the file test.txt has 7 lines of content, what will the following expression return?
import io
# create a multi-line string and pass it into StringIO
f = io.StringIO('''first line
second line
third
fourth
fifth
6
7''')
con=f.read(7)
print(con)

print(len(f.readlines()))
