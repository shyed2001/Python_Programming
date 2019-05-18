print('''
%	Modulus - remainder of the division of left operand by the right
	x % y (remainder of x/y)
//	Floor division - division that results into whole number adjusted
 to the left in the number line	x // y
''')
print('''
The % (modulo) operator yields the remainder from the division of
the first argument by the second. The numeric arguments are first
 converted to a common type. A zero right argument raises the
ZeroDivisionError exception. The arguments may be floating point
numbers, e.g., 3.14%0.7 equals 0.34
(since 3.14 equals 4*0.7 + 0.34.)
The modulo operator always yields a result with the same sign
as its second operand (or zero); the absolute value of the
result is strictly smaller than the absolute value of the second
operand [2].
Taken from http://docs.python.org/reference/expressions.html

 The first number is the numerator and the second is the denominator. In our example
2 divided by 6 is 0 remainder 2, therefore the result is 2.
print(2%6)
This is how it's implemented in Python:
a % b = a - b * floor(a/b)
a=2
b=6
print(a % b = a - b * floor(a/b))
''')
print('''
To use floor convertor we have to import from Math
from math import *
''')
from math import *
a=2
b=6
print(a - b * floor(a/b))
print('''
print(2%6)
''')
print(2%6)

print('''
a=12
b=15
print(a - b * floor(a/b))
''')
a=12
b=15
print(a - b * floor(a/b))
print('''
print(12%15)
''')

print(12%15)

print('''
a=12
b=-15
print(a - b * floor(a/b))
''')
a=12
b=-15
print(a - b * floor(a/b))
print('''
print(12%-15)
''')

print(12%-15)

print('''
a=-12
b=-15
print(a - b * floor(a/b))
''')
a=-12
b=-15
print(a - b * floor(a/b))
print('''
print(-12%-15)
''')
print(-12%-15)

print('''
a=6
b=6
print(a - b * floor(a/b))
''')
a=6
b=6
print(a - b * floor(a/b))
print('''
print(6%6)
''')
print(6%6)

print('''
a=1
b=6
print(a - b * floor(a/b))
''')
a=1
b=6
print(a - b * floor(a/b))
print('''
print(1%6)
''')
print(1%6)

print('''
a=-1
b=6
print(a - b * floor(a/b))
''')

print('''
print(-1%6)
''')
print(-1%6)

print('''
a=-1
b=-6
print(a - b * floor(a/b))
''')
a=-1
b=-6
print(a - b * floor(a/b))
print('''
print(-1%-6)
''')
print(-1%-6)

print('''
a=0
b=5
print(a - b * floor(a/b))
''')

print('''
print(0%5)
''')
print(0%5)
print('''
a=2
b=-6
print(a - b * floor(a/b))
''')
a=2
b=-6
print(a - b * floor(a/b))
print('''
print(2%-6)
''')
print(2%-6)
print('''
a=-2
b=6
print(a - b * floor(a/b))
''')
print('''
print(-2%6)
''')

print(-2%6)

print('''
a=-7
b=1
print(a - b * floor(a/b))
''')
a=-7
b=1
print(a - b * floor(a/b))
print('''
print(-7%1)
''')
print(-7%1)

print('''
print(7%0)
will produce error essage
ZeroDivisionError
''')



print('''
Somewhat off topic, the % is also used in string formatting operations
like %= to substitute values into a string:

>>> x = 'abc_%(key)s_'
>>> x %= {'key':'value'}
>>> x
'abc_value_'
Again, off topic, but it seems to be a little documented feature which took me
 awhile to track down, and I thought it was related to Pythons modulo
  calculation for which this SO page ranks highly.

''')
print('''
d="dog %(bark)s"
d %= {'bark':'run'}
print(d)
''')
d="dog %(bark)s"
d %= {'bark':'run'}
print(d)

print('''
b="bag%(heavy)s"
b %= {'heavy':'light'}
print(b)
''')
b="bag%(heavy)s"
b %= {'heavy':'light'}
print(b)



print('''
The modulus is a mathematical operation, sometimes described
as "clock arithmetic." I find that describing it as simply a
remainder is misleading and confusing because it masks the real
reason it is used so much in computer science. It really is used
 to wrap around cycles.

Think of a clock: Suppose you look at a clock in "military" time,
 where the range of times goes from 0:00 - 23.59. Now if you wanted
something to happen every day at midnight, you would want the current
 time mod 24 to be zero:

if (hour % 24 == 0):

You can think of all hours in history wrapping around a circle of
24 hours over and over and the current hour of the day is that
infinitely long number mod 24. It is a much more profound concept
than just a remainder, it is a mathematical way to deal with cycles
and it is very important in computer science. It is also used to
wrap around arrays, allowing you to increase the index and use
the modulus to wrap back to the beginning after you reach the end
 of the array.


This is how it's implemented in Python:
a % b = a - b * floor(a/b)


print("""
divmod(a, b)
Take two (non complex) numbers as arguments and return
 a pair of numbers consisting of their quotient and remainder
  when using long division.
""")

''')

print('''
from math import *
a=2
b=6
print(a - b * floor(a/b))

print(2%6)
''')
from math import *
a=2
b=6
print(a - b * floor(a/b))

print(2%6)

print('''
a=24
b=7
print(divmod(a, b))
print(a/ b)
print(a// b)
print(a% b)
''')
a=24
b=7
print(divmod(a, b))
print(a/ b)
print(a// b)
print(a% b)

print('''
a=-4
b=7
print(divmod(a, b))
print(a/ b)
print(a// b)
print(a% b)
''')
a=-4
b=7
print(divmod(a, b))
print(a/ b)
print(a// b)
print(a% b)

print('''
% Modulo operator can be also used for printing strings
 (Just like in C) as defined on Google
https://developers.google.com/edu/python/strings.

      # % operator
text = ("%d little pigs come out or I'll %s and %s and %s"
% (3, 'huff', 'puff', 'blow down'))
print(text)
This seems to bit off topic but It will certainly help someone.
''')
text = ("%d little pigs come out or I'll %s and %s and %s"
% (3, 'huff', 'puff', 'blow down'))
print(text)

print('''
Floor Division(//) - The division of operands where the result is the quotient
 in which the digits after the decimal point are removed. But if one of the
 operands is negative, the result is floored, i.e.,
 rounded away from zero (towards negative infinity): examples: 9//2 = 4 and
 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
Towards infinity and away from zero are different things.
Example for (-1.2 and 3.4): "flooring" is towards
 negative infinity (-2 and 3), "truncating" is towards zero
 (-1 and 3), "saturating" is away from zero (-2 and 4),
 and "ceiling" is towards positive infinity (-1 and 4).
 ''')

print('''
%	Modulus - remainder of the division of left operand by the right
	x % y (remainder of x/y)
//	Floor division - division that results into whole number adjusted
 to the left in the number line	x // y

 from math import *
a=-6
b=4
print(floor(a/b))
print(-6//4)
print(-6%4)

print(a - b * floor(a/b))

a=24
b=7
print(divmod(a, b))
print(a/ b)
print(a// b)
print(a% b)
''')
from math import *
a=-6
b=4
print(floor(a/b))
print(-6//4)
print(-6%4)

print(a - b * floor(a/b))

a=24
b=7
print(divmod(a, b))
print(a/ b)
print(a// b)
print(a% b)

print("""
how does remainder or  modulus operator works


a % b = a - b * floor(a/b)


An expression like x % y evaluates to the remainder of x ÷ y.
Precedence is the same as operators / (division) and * (multiplication).

>>> 9 / 2
4
>>> 9 % 2
1




% Modulo operator can be also used for printing strings (Just like in C)
 as defined on Google https://developers.google.com/edu/python/strings.

      # % operator
  text = "%d little pigs come out
 or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')

This seems to bit off topic but It will certainly help someone.


Somewhat off topic, the % is also used in string formatting operations
like %= to substitute values into a string:

>>> x = 'abc_%(key)s_'
>>> x %= {'key':'value'}
>>> x
'abc_value_'
Again, off topic, but it seems to be a little documented feature which took
me awhile to track down, and I thought it was related to Pythons modulo
 calculation for which this SO page ranks highly.




Also, there is a useful built-in function called divmod:

divmod(a, b)

Take two (non complex) numbers as arguments and return a pair of numbers

consisting of their quotient and remainder when using long division.





""")
