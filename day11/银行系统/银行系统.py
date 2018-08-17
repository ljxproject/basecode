'''
类:

类名:  程序界面类
属性:
方法:  显示欢迎页面,         显示登录页面进行登陆,          显示主程序界面,

类名: user
属性: 名字,身份证号,手机号,---卡
方法:

类名: 卡card
属性: 卡号,密码,金额
方法:

类名: bankFunc
属性:
方法: 开户,查询,存款,取款,转账,改密,锁定,解锁,补卡,注销,退出

'''
from time import sleep

import adminView
from bankFunc  import  BankFunc
import pickle
import os

# main函数,作为程序的入口
def main():
    adminView.welcomView()
    if adminView.loginView() == -1: #表示登陆失败
#       作业: 重新登陆,一般出错3次后,则程序直接退出
        pass

  # 表示登陆成功

    # 从文件中获取所有的用户信息
    path = os.path.join(os.getcwd(), "alluser.txt")
    # 判断该文件是否存在
    if not os.path.exists(path): #如果该文件不存在
        # 不存在用户信息时,传入一个空的字典
        bank = BankFunc({})
    else: #存在
        rf = open(path,"rb")
        # 读取alluser
        alluser = pickle.load(rf)
        # 创建银行功能对象
        bank = BankFunc(alluser)

    while True:
    #     显示主功能页面
        adminView.funcView()
        funcNumber = input("请输入您要选择的功能:")
        if funcNumber == "1":#开户
            bank.createUser()
        elif funcNumber == "2":#查询
            bank.queryMoney()
        elif funcNumber == "3":#存款
            bank.saveMoney()
        elif funcNumber == "4":#取款
            bank.getMoney()
        elif funcNumber == "5":#转账
            bank.translateMoney()
        elif funcNumber == "6":#改密
            bank.editPasswd()
        elif funcNumber == "7":#锁定
            bank.lockCard()
        elif funcNumber == "8":#解锁
            bank.unlockCard()
        elif funcNumber == "9":#补卡
            bank.fillCard()
        elif funcNumber == "0":#注销
            bank.killCard()
        elif funcNumber == "q": #退出
        #    验证

        #     将所有的用户信息存储到文件中去
            # 打开一个文件
            # 获取保存路径
            wf = open(path,"wb")
            pickle.dump(bank.allUser,wf)

            print("您正在退出银行系统...")
            sleep(1.5)
            print("退出成功")
            break
        else:
            print("您输入的不正确")


# 测试
def test():
    # 创建银行功能对象
    bank = BankFunc()
    print(bank.createCardNumber())


if __name__ == '__main__':
    main()
    # test()












