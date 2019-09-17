from math import *

print('''
print(floor(4))
print(floor(9.0))
print(floor(9.5))
print(floor(9,5)) # error)
''')
print(floor(4))
print(floor(9.0))
print(floor(9.5))
# error) print(floor(9,5))
print('''
print(floor(4.7))
print(floor(9.3))
print(floor(9.6))
print(floor(-4.7))
print(floor(-9.3))
print(floor(-9.6))
''')
print(floor(4.7))
print(floor(9.3))
print(floor(9.6))
print(floor(-4.7))
print(floor(-9.3))
print(floor(-9.6))

print('''
Towards infinity and away from zero are different things.
Example for (-1.2 and 3.4): "flooring" is towards
 negative infinity (-2 and 3), "truncating" is towards zero
 (-1 and 3), "saturating" is away from zero (-2 and 4),
 and "ceiling" is towards positive infinity (-1 and 4).
 ''')

print('''
print(ceil(4))
print(ceil(9.0))
print(ceil(4,5) # error)
print(ceil(9,0) # error)
''')
#print(ceil(4,5)) # error
# error print(ceil(9,0))
print(ceil(4))
print(ceil(9.0))
print('''
print(ceil(4.7))
print(ceil(9.3))
print(ceil(9.6))
print(ceil(9.5))
print(ceil(-4.7))
print(ceil(-9.3))
print(ceil(-9.6))
print(ceil(-9.5))
''')
print(ceil(4.7))
print(ceil(9.3))
print(ceil(9.6))
print(ceil(9.5))
print(ceil(-4.7))
print(ceil(-9.3))
print(ceil(-9.6))
print(ceil(-9.5))
print('''
print(round(4,7))
print(round(9,3))
''')
print(round(4,7))
print(round(9,3))
print('''
print(round(4.7))
print(round(9.3))
print(round(9.6))
print(round(9.5))
print(round(-4.7))
print(round(-9.3))
print(round(-9.6))
print(round(-9.5))
''')
print(round(4.7))
print(round(9.3))
print(round(9.6))
print(round(9.5))
print(round(-4.7))
print(round(-9.3))
print(round(-9.6))
print(round(-9.5))
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