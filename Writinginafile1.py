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
with open("G:/PyWorkDirectory/2PAGLA2.txt", "w") as fl11:
    pass
print(""" with open("G:/PyWorkDirectory/2PAGLA2.txt", "w") as fl11:
    pass
that code block will only create the file """)

print(""" with open("G:/PyWorkDirectory/2PAGLA2.txt", "w") as fl11:
    fl11.write("rrrr")
that code block will create the file and write rrrr to it""")

with open("G:/PyWorkDirectory/2PAGLA2.txt", "w") as fl11:
    fl11.write("rr/nrrrr")
    fl11.write("RR\nRRRR")
    print(""""
    fl1.seek(o) start to write the file from begineening again""")
    fl11.seek(0)
    fl11.write("WWrite")
    fl11.write("\nwww\nWWW/nwww/nWWWrite after seek /0")
print(""" with open("G:/PyWorkDirectory/2PAGLA2.txt", "a") as fl11:
    fl11.write("rrrr")
that code block will create the file and write rrrr to it, a insted of w is
 used to append= write at the end of existing data""")

with open("G:/PyWorkDirectory/2PAGLA2.txt", "a") as fl11:
    fl11.write("rr/nrrrr")
    fl11.write("RR\nRRRR/nrRrRrRrRappend")

print(""" to read and copy a file and write/create that copy file line by line
we use -
with open("G:/PyWorkDirectory/2PAGLA2.txt", "r") as rf:
    with open("G:/PyWorkDirectory/2PAGLA2rfwfcopy.txt", "w") as wf:
        for line in rf:
            wf.write(line)
""")
with open("G:/PyWorkDirectory/2PAGLA2.txt", "r") as rf:
    with open("G:/PyWorkDirectory/2PAGLA2rfwfcopy.txt", "w") as wf:
        for line in rf:
            wf.write(line)

print(""" To copy and write/create an image file the code will be
with open("G:/PyWorkDirectory/640px-Computer_system_bus.svg.png", "rb") as rbf:
    with open("G:/PyWorkDirectory/copyOF640px-Computer_system_buscopyOF.svg.png", "wb") as wbf:
        for line in rbf:
            wbf.write(line)
rb an wb is used insted of r and w
""")

with open("G:/PyWorkDirectory/640px-Computer_system_bus.svg.png", "rb") as rbf:
    with open("G:/PyWorkDirectory/copyOF640px-Computer_system_buscopyOF.svg.png", "wb") as wbf:
        for line in rbf:
            wbf.write(line)

print(""" reading the picture png file in binary mode chunk by chunk and
copy and create that file-
with open("G:/PyWorkDirectory/640px-Computer_system_bus.svg.png", "rb") as rbf:
    with open("G:/PyWorkDirectory/ChunksizecopyOF640px-Computer_system_buscopyOF.svg.png", "wb") as wbf:
        chunk_size= 2560
        rbf_chunk=rbf.read(chunk_size)
        while len(rbf_chunk)> 2500:
            wbf.write(rbf_chunk)
            wbf.tell()
            rbf_chunk=rbf.read(chunk_size)
as the file does not write all the binary bites, there will some part of the
 picture missing something.
""")


with open("G:/PyWorkDirectory/640px-Computer_system_bus.svg.png", "rb") as rbf:
    with open("G:/PyWorkDirectory/ChunkSizecopyOF640px-Computer_system_buscopyOF.svg.png", "wb") as wbf:
        chunk_size= 2560
        rbf_chunk=rbf.read(chunk_size)
        while len(rbf_chunk)> 2000:
            wbf.write(rbf_chunk)
            wbf.tell()
            rbf_chunk=rbf.read(chunk_size)
print(""" reading the picture png file in binary mode chunk by chunk and
copy and create that file-
with open("G:/PyWorkDirectory/640px-Computer_system_bus.svg.png", "rb") as rbf:
    with open("G:/PyWorkDirectory/chunksiz640px-Computer_system_buscopyOF.svg.png", "wb") as wbf:
        chunk_size= 4000
        rbf_chunk=rbf.read(chunk_size)
        while len(rbf_chunk)> 2500:
            wbf.write(rbf_chunk)
            wbf.tell()
            rbf_chunk=rbf.read(chunk_size)
as the file does not write all the binary bites, there will some part of the
 picture missing something.
""")
with open("G:/PyWorkDirectory/640px-Computer_system_bus.svg.png", "rb") as rbf:
    with open("G:/PyWorkDirectory/chunksiz640px-Computer_system_buscopyOF.svg.png", "wb") as wbf:
        chunk_size= 4000
        rbf_chunk=rbf.read(chunk_size)
        while len(rbf_chunk)> 2500:
            wbf.write(rbf_chunk)
            wbf.tell()
            rbf_chunk=rbf.read(chunk_size)


with open("G:/PyWorkDirectory/640px-Computer_system_bus.svg.png", "rb") as rbf:
    with open("G:/PyWorkDirectory/Computer_system_buscopyOF.svg.png", "wb") as wbf:
        chunk_size= 4000
        rbf_chunk=rbf.read(chunk_size)
        while len(rbf_chunk)> 0:
            wbf.write(rbf_chunk)
            wbf.tell()
            rbf_chunk=rbf.read(chunk_size)

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