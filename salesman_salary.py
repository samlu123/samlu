#!/usr/bin/env python3
'''计算相机销售人员的工资：
基本工资1500，每售出一台相机可以得到200并获得2%的抽成。程序要求输入相机数列及单价'''

basic_salary = 1500

bonus_rate = 200

commision_rate = 0.02

number_of_camera = int(input('enter the number of inputs sold:'))

price = float(input('enter the total prices:'))

bonus = (bonus_rate * number_of_camera)

commision = (commision_rate * number_of_camera)

print('Bonus = {:6.2f}'.format(bonus))
print('commision = {:6.2f}'.format(commision))
print('gross salary = {:6.2f}'.format(basic_salary + bonus + commision))

