#!/usr/bin/env python3

sticks = 21

print('There are 21 sticks, you can take 1-4 number of sticks at a time.')

print('Whoever will take the last stick will loose.')

while True:
    print('Sticks left: ',sticks)
    sticks_taken = int (input('take sticks(1-4):'))
    if sticks ==1:
        print('you took the last stick, you loose')
        break
    if sticks_taken >=5 or sticks_taken <=0:
        print ('wrong choice')
        continue
    print('computer took: ',(5-sticks_taken),'\n')
    sticks -=5

