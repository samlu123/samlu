#!/usr/bin/env python3
# 在一定年限下的本金复利

amount = float(input('Enter amount: ')) #输入金额

inrate = float(input('Enter Interest rate: ')) #输入利率

period = int(input('Enter period: ')) #输入期限

value = 0

year = 1

while year <= period:
    value = amount +(inrate * amount)
    print('Year {} Rs. {:.2f}'.format(year,value))
    amount = value
    year += 1
