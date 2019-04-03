print('''
impost Students module fron student file by
print(student1.on_honor_roll())
''')
from student import Students

print(''' Make two student objects
student1 = Students("Alan", "Aerospace", 3.5)
student2 = Students("Akil", "Art", 3.3)
''')
student1 = Students("Alan", "Aerospace", 3.5)
student2 = Students("Akil", "Art", 3.3)

print(''' TO see if they are on honor roll or not
print(student1.on_honor_roll())

print(student2.on_honor_roll())
''')

print(student1.on_honor_roll())

print(student2.on_honor_roll())