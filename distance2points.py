# Created:     01/05/2019
# Copyright:   (c) User 2019
# Licence:     <your licence>


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx*dx + dy*dy
    #result = dsquared**0.5
    result = pow(dsquared,0.5)
    return result
print(distance(1, 2, 4, 6))

import math

def distance(x1, y1, x2, y2):
 return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

print(distance(1, 2, 4, 6))