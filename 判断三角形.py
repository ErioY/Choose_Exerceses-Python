'''
@Autor: ErioY
@Date: 2019-10-16 20:55:36
@Email: 1973545559@qq.com
@Github: https://github.com/ErioY
@LastEditors: ErioY
@LastEditTime: 2019-10-16 21:51:54
'''
# 通过Input（）函数任意输入三条边长，经过简单的计算后，判断三条边长能否构成三角形，并确定是类型的三角形，如（等边，等腰，一般三角形）
print("请分别输入三角形的三条边长：")
# a = int(input("第一条边："))
# b = int(input("第二条边："))
# c = int(input("第三条边："))
a = 3
b = 3
c = 4
if (a <= 0 or b <= 0 or c <= 0):
    print("输入有误！请重新输入三角形的三条边长：")
    a = input("第一条边：")
    b = input("第二条边：")
    c = input("第三条边：")
if (a + b > c and a + c > b and b + c > a):
    if (a == b or a == c or b == c):
        if (a == b and a == c and b == c):
            print("这是等边三角形")
        else:
            print("这是等腰三角形")
    else:
        print("这是一般三角形")
else:
    print("不能构成三角形")