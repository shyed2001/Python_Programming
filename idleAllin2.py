Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2-1
1
>>> 10/3
3.3333333333333335
>>> print(("10/3")+ "=" + str(10/3))
10/3=3.3333333333333335
>>> print("idleAllin2.py")
idleAllin2.py
>>> print("==============================================\n==========================\n=====================")
==============================================
==========================
=====================
>>> print(("-10/3")+ "=" + str(-10/3))
-10/3=-3.3333333333333335
>>> print(("10/-3")+ "=" + str(10/-3))
10/-3=-3.3333333333333335
>>> print(("9.73800000000")+ "=" + str(9.73800000000))
9.73800000000=9.738
>>> print(("9.738043625475237500")+ "=" + str(9.738043625475237500))
9.738043625475237500=9.738043625475237
>>> print(("9.73804362547523750082364862865821")+ "=" + str(9.73804362547523750082364862865821))
9.73804362547523750082364862865821=9.738043625475237
>>>  print(("10**3")+ "=" + str(10**3))
SyntaxError: unexpected indent
>>> print(("10**3")+ "=" + str(10**3))
10**3=1000
>>> print(("10//3")+ "=" + str(10//3))
10//3=3
>>> print(("10%3")+ "=" + str(10%3))
10%3=1
>>> print(("Quotient of")("10//3")+ "=" + str(10//3))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(("Quotient of")("10//3")+ "=" + str(10//3))
TypeError: 'str' object is not callable
>>> print(("Quotient of")+("10//3")+ "=" + str(10//3))
Quotient of10//3=3
>>> print(("Remainder of")+("10%3")+ "=" + str(10%3))
Remainder of10%3=1
>>> "\""
'"'
>>> print(("\"")+ "=" + str("\""))
"="
>>> 2+3
5
>>> print(("\""))
"
>>> print("\"")
"
>>> print(("Hallow  world"))
Hallow  world
>>> print('Don/'t go there')
	  
SyntaxError: invalid syntax
>>> print('Don\'t go there')
	  
Don't go there
>>> print("Don\'t go there")
	  
Don't go there
>>> print("Don't go there")
	  
Don't go there
>>> print('Don't go there')
	  
SyntaxError: invalid syntax
>>> print('Don"t go there')
	  
Don"t go there
>>> print("Don\"t go there")
	  
Don"t go there
>>> print("Don\	t go there")
	  
Don\	t go there
>>> print("Don\t go there")
	  
Don	 go there
>>> print(("Hallow\nworld"))
	  
Hallow
world
>>> print(("Hallow
	   
SyntaxError: EOL while scanning string literal
>>> print(("Hallow
       world"))
	   
SyntaxError: EOL while scanning string literal
>>> print(("Hallow  \n  world"))
	   
Hallow  
  world
>>> print(("Hallow")
	  (world"))
	   
SyntaxError: EOL while scanning string literal
>>> print(("Hallow")
	  ("world"))
	   
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    ("world"))
TypeError: 'str' object is not callable
>>> print(("Hallow""world"))
	  
Hallowworld
>>> print(("Hallow"
	   "world"))
	  
Hallowworld
>>> print(("Hallow")+
	   ("world"))
	  
Hallowworld
>>> print(("Hallow \n world"))
	  
Hallow 
 world
>>> print("""Hallow"+
	   world""")
	  
Hallow"+
	   world
>>> print("""Hallow"""
	   """world""")
	  
Hallowworld
>>> print("""Hallow
	   world""")
	  
Hallow
	   world
>>> input('Enter something please')
	  
Enter something pleaseg
'g'
>>> input('Enter something please: ')
	  
Enter something please: d\n
'd\\n'
>>> input('Enter something please: ')
	  
Enter something please: r
'r'
>>> input('Enter something please: ')
	  
Enter something please: d\ng
'd\\ng'
>>> input('Enter something please: ')
	  
Enter something please: ffff
'ffff'
>>> input('Enter something please: ')
	  
Enter something please: g
'g'
>>> g
	  
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    g
NameError: name 'g' is not defined
>>> input('To continue \n- Enter something please: ')
	  
To continue 
- Enter something please: k\nh
'k\\nh'
>>> input('To continue \n- Enter something please:____ ')
	  
To continue 
- Enter something please:____ l\k
'l\\k'
>>> input('To continue \n- Enter something please:____ ')
	  
To continue 
- Enter something please:____ mm
'mm'
>>> output('To continue \n- Enter something please:____ ')
	  
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    output('To continue \n- Enter something please:____ ')
NameError: name 'output' is not defined
>>> output(1+1)
	  
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    output(1+1)
NameError: name 'output' is not defined
>>> print("Hallow, world")
	  
Hallow, world
>>> print("2" + "3")
	  
23
>>> print("2.0" + "3.0")
	  
2.03.0
>>> print("Fun" * "3.0")
	  
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print("Fun" * "3.0")
TypeError: can't multiply sequence by non-int of type 'str'
>>> print("Fun" * 3)
	  
FunFunFun
>>> print("2" * "3")
	  
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print("2" * "3")
TypeError: can't multiply sequence by non-int of type 'str'
>>> print("2" * 3)
	  
222
>>> print("Fun" * 3.0)
	  
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print("Fun" * 3.0)
TypeError: can't multiply sequence by non-int of type 'float'
>>> print("2" * 3.0)
	  
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print("2" * 3.0)
TypeError: can't multiply sequence by non-int of type 'float'
>>> print("Fun" * 0)
	  

>>> print("9" * 0)
	  

>>> print("9" * 0.0)
	  
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print("9" * 0.0)
TypeError: can't multiply sequence by non-int of type 'float'
>>> print(("("Fun" * 0)")+ "=" + str(("Fun" * 0)))
	  
SyntaxError: invalid syntax
>>> print(("(Fun * 0)")+ "=" + str(("Fun" * 0)))
	  
(Fun * 0)=
>>> print(("(9 * 0)")+ "=" + str("9" * 0))
	  
(9 * 0)=
>>> print(("(\"Fun\" * 0)")+ "=" + str(("Fun" * 0)))
	  
("Fun" * 0)=
>>> print(("(\"9\" * 0)")+ "=" + str("9" * 0))
	  
("9" * 0)=
>>> 
