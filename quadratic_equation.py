#!/usr/bin/env python3
#二元方程的解
import math

a = int(input('enter value of a: '))
b = int(input('enter value of b: '))
c = int(input('enter value of c: '))
d = b * b - 4 * a * c

if d < 0:
    print('NO roots')

else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)

    print('root1 = ',root1)
    print('root2 = ',root2)

