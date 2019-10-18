'''
@Autor: ErioY
@Date: 2019-10-16 20:56:13
@Email: 1973545559@qq.com
@Github: https://github.com/ErioY
@LastEditors: ErioY
@LastEditTime: 2019-10-18 11:50:43
'''
# 设有三个变量a,b,c,分别对三个变量赋值，并对三个变量进行排序。如a=5,b=7,c=6,则排序结果为b>c>a
# a = int(input("请输入第一个值："))
# b = int(input("请输入第二个值："))
# c = int(input("请输入第三个值："))
a = 5
b = 7
c = 6
num = {
    "a": a,
    "b": b,
    "c": c
}
num = sorted(num.items(), key=lambda m: m[1], reverse=True)
print("升序结果为：", num[0][0], ">", num[1][0], ">", num[2][0])
print(num)