
print('''
Inheritance is where we can define some attributes & functions inside
of a class then define another class and inherite all of those attributes.
A class will ahve all the functionality of another class without having to write
all those codes and methods.
''')

from Chef import Chef

myChef = Chef()

myChef.make_chicken()
myChef.make_special_dish()
print("Chef Chef end")

from Chef import ChineseChef
from ChineseChef import ChineseChef
myChineseChef = ChineseChef()

myChineseChef.make_chicken()
myChineseChef.make_special_dish()
myChineseChef.make_Fried_rice()

print("Chef ChineseChef end")



myChineseChef.make_chicken()
myChineseChef.make_special_dish()
myChineseChef.make_Fried_rice()
print("ChineseChef ChineseChef end")

