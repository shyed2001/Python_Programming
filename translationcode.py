#translationcode.py

print('''
Basic translator in python
''')
print('''
Basic translator in python
''')

print('''
evry vowel in the phrase will become g
like example, gog will ggg, dog will be dgg, bag will be bgg, etc
''')


print('''
Basic translator in python v 1.11
''')
print('''
Basic translator in python v 1.11
''')

print('''
def translation(words):
 translation=""
 for letter in words:
    if letter in "AEIOUaeiou":
        translation= translation + "g"
    else:
         translation= translation + letter
 return translation
print(translation(input("please input word/s:   " )))

''')

def translation(words):
 translation=""
 for letter in words:
    if letter in "AEIOUaeiou":
        translation= translation + "g"
    else:
         translation= translation + letter
 return translation
print(translation(input("please input word/s:   " )))



print('''
Basic translator in python v 1.22
''')
print('''
Basic translator in python v 1.22

def translation(words):
 translation=""
 for letter in words:
    if letter.lower() in "aeiou":
       if letter.isupper():
          translation= translation + "G"
       else:
         translation= translation + "g"
    else:
         translation= translation + letter
 return translation
words=input("please input word/s:   " )
print("you entered - ", words)
print( " The translation is " , translation(words))
''')



def translation(words):
 translation=""
 for letter in words:
    if letter.lower() in "aeiou":
       if letter.isupper():
          translation= translation + "G"
       else:
         translation= translation + "g"
    else:
         translation= translation + letter
 return translation
words=input("please input word/s:   " )
print("you entered - ", words)
print( " The translation is " , translation(words))



print('''
''')

print('''
''')


print('''
''')
