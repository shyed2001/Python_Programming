print('''
In python, you can put ‘j’ or ‘J’ after a number to make it imaginary, 
so you can write complex literals easily:
''')
print(1j)
print(1J)
print(1j * 1j)
print('''
The ‘j’ suffix comes from electrical engineering, 
where the variable ‘i’ is usually used for current.
 (Reasoning found here.)
The type of a complex number is complex, and you can use
 the type
 as a constructor if you prefer:
''')
print(complex(2,3))

A complex number has some built-in accessors:

>>> z = 2+3j
>>> z.real
2.0
>>> z.imag
3.0
>>> z.conjugate()
(2-3j)
Several built-in functions support complex numbers:

>>> abs(3 + 4j)
5.0
>>> pow(3 + 4j, 2)
(-7+24j)
The standard module cmath has more functions that handle complex numbers:

>>> import cmath
>>> cmath.sin(2 + 3j)
(9.15449914691143-4.168906959966565j)
shareedit
edited May 23 '17 at 12:10

Community♦
11
answered Dec 3 '11 at 20:20

rob mayoff
297k42598647
5
'i' is also used by mathematicians, physicists, and nearly all other scientists. If that isn't confusing enough, some use 'i' to represent the "positive" square root of one, whereas 'j' is the "negative" square root of one. Thus i == -j. FYJ... – jvriesem Sep 16 '16 at 4:28 
add a comment

 
12

The following example for complex numbers should be self explanatory including the error message at the end

>>> x=complex(1,2)
>>> print x
(1+2j)
>>> y=complex(3,4)
>>> print y
(3+4j)
>>> z=x+y
>>> print x
(1+2j)
>>> print z
(4+6j)
>>> z=x*y
>>> print z
(-5+10j)
>>> z=x/y
>>> print z
(0.44+0.08j)
>>> print x.conjugate()
(1-2j)
>>> print x.imag
2.0
>>> print x.real
1.0
>>> print x>y

Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    print x>y
TypeError: no ordering relation is defined for complex numbers
>>> print x==y
False
>>> 
