#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     30/03/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print('''
secret_word="girrafe"
guess=""

while guess!= secret_word:
      guess=input("""Enter guess, Guessing game1.11""")
print("you win")
''')
print("Guessing game 1")
print("Guessing game 1.11")

secret_word="girrafe"
guess=""

while guess!= secret_word:
      guess=input("""Enter guess, Guessing game1.11""")
print("you win")


print("Guessing game 1.22")
print("Guessing game 1.22")

print('''
esc = False
secret_word="girrafe"
guess=""
win=False
while guess!= secret_word and not(esc):
      if guess!="e":
         guess=input("""Enter guess, Guessing game1.22 or
         enter e to exit:       """)
      else:
        esc=True
if esc:
   print("You exit")
else:
     print("you win")
''')
esc = False
secret_word="girrafe"
guess=""
while guess!= secret_word and not(esc):
      if guess!="e":
         guess=input("""Enter guess, Guessing game1.22 or
         enter e to exit:       """)
      else:
        esc=True
if esc:
   print("You exit")
else:
     print("you win")


print("Guessing game 2")
print("Guessing game 2.1")

print('''

secret_word="girrafe2"
guess=""
guess_count=0
out_of_guesses=False
guess_limit=3
while guess!= secret_word and not(out_of_guesses):
      if guess_count< guess_limit:
        guess=input("Enter guess, for guessing game 2.1, maximum 3 times:   ")
        guess_count+=1
      else:
         out_of_guesses=True

if out_of_guesses:
   print("you lose")
else:
 print("you win")
''')

secret_word="girrafe2"
guess=""
guess_count=0
out_of_guesses=False
guess_limit=3
while guess!= secret_word and not(out_of_guesses):
      if guess_count< guess_limit:
        guess=input("Enter guess, for guessing game 2.1, maximum 3 times:   ")
        guess_count+=1
      else:
         out_of_guesses=True

if out_of_guesses:
   print("you lose")
else:
 print("you win")


print('''
''')

print('''
''')

print('''
''')

