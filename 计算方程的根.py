'''
@Autor: ErioY
@Date: 2019-10-16 20:57:02
@Email: 1973545559@qq.com
@Github: https://github.com/ErioY
@LastEditors: ErioY
@LastEditTime: 2019-10-18 12:08:53
'''
# 计算一元二次方程ax2+bx+c 的根是公式。因为负数的平方根是虚的，所以可以使用平方根里面的表达式（称为差别式）先进地判别，检查根型。
# 如果判别式是负数，根是虚的。
# 如果判别式是零，只有一个根；
# 如果判别式是正的，有两个根。
# 写一个程序，使用二次方根式得到实根，即忽略虚根。使用判别式确定有一个根或两个根，然后显示出答案
import math
print("请分别输入a, b, c：")
# a = int(input("a："))
# b = int(input("b："))
# c = int(input("c："))
a = 1
b = 2
c = 1
judge = b ** 2 - 4 * a * c
if judge < 0:
    print("该方程无实根")
else:
    if judge == 0:
        x = (- b + math.sqrt(judge)) / 2 * a
        print("该方程有一个根: x1 = x2 = ", x)
    else:
        x1 = (- b + math.sqrt(judge)) / 2 * a
        x2 = (- b - math.sqrt(judge)) / 2 * a
        print("该方程有两个根：x1 = ", x1, ", x2 = ", x2)