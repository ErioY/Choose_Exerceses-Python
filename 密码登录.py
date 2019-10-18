'''
@Autor: ErioY
@Date: 2019-10-16 20:55:52
@Email: 1973545559@qq.com
@Github: https://github.com/ErioY
@LastEditors: ErioY
@LastEditTime: 2019-10-16 22:07:29
'''
# 密码登录程序
# 要求：建立一个登录窗口,要求输入帐号和密码。
# 设定用户名为”zhangshan”，密码为“Python123”;
# 若用户名正确，密码正确，则显示 “Zhangshan先生，欢迎你 !”;
# 如果用户名错误，则显示“用户名错误，请重新输入! ”; 若密码不正确,显示“对不起,密码错误,无法登录! ”
# user = input("请输入账号：")
# password = input("请输入密码：")
user = "zhangshan"
password = "123"
user1 = "zhangshan"
password1 = "Python123"
while(True):
    if (user == user1):
        if (password == password1):
            print("Zhangshan先生，欢迎你!")
            break
        else:
            print("对不起,密码错误,无法登录!")
            break
    else:
        # user = input("用户名错误，请重新输入：")
        print("用户名错误")

