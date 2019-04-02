

print(''' To only read an external file
works_file=open("works.txt","r")
''')
works_file=open("works.txt","r")

print(''' To only read and write  an external fil
works_file=open("works.txt","r+")
''')
works_file=open("works.txt","r+")



print(''' To only write  an external fil
works_file=open("works.txt","w")
''')
works_file=open("works.txt","w")


print(''' To only write at the end or append at  an external fil
works_file=open("works.txt","a")
''')
works_file=open("works.txt","a")


print('''
TO find out if the file is readable or not
print(works_file.readable())
''')
print(works_file.readable())

print(''' TO read the whole ,file
print(works_file.read())
''')
print(works_file.read())


print(''' to read only the first line
print(works_file.readline())
''')
print(works_file.readline())

print(''' to read only the first three line together
print(works_file.readline())
print(works_file.readline())
print(works_file.readline())
''')
print(works_file.readline())
print(works_file.readline())
print(works_file.readline())


print(''' to read all line together in a list
print(works_file.readlines())
''')
print(works_file.readlines())

print(''' to read the 3rd or indexed 2nd line in a list
print(works_file.readlines()[2])
''')
print(works_file.readlines()[2])


print(''' TO close the file
works_file.close()
''')

works_file.close()

print('''

''')

print('''

''')

print('''

''')
print('''
To append a file
works_file=open("works.txt","a")

''')
works_file=open("works.txt","a")

print('''
TO write in the file
works_file.write(" \n read books 10:00")
''')
works_file.write(" \n read books 10:00")


print('''
To write a file in or overwrite the/ a file
create a new file named works222.txt
works_file=open("works222.txt","w")

''')

works_file=open("works222.txt","w")

print('''
To write a file in or overwrite the/ a file
create a new file named works333.txt
works_file=open("works333.txt","w")

''')

works_file=open("works333.txt","w")
print('''
TO write in the file
works_file.write(" \n read books 10:00")
''')
works_file.write(" \n read books 10:00")

print('''
To write a file in or overwrite the/ a file
create a new file named works333.txt
works_file=open("works444.html","w")

''')

works_file=open("works444.html","w")
print('''
TO write in the file
works_file.write(" <p> This is HTML <p>")
''')
works_file.write(" <p> This is HTML <p> ")

print(''' TO close the file
works_file.close()
''')

works_file.close()

print('''

''')