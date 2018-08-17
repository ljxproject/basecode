import random
from card import Card
from user import User


class BankFunc(object):
    # 方法: 开户, 查询, 存款, 取款, 转账, 改密, 锁定, 解锁, 补卡, 注销, 退出

    # 需要一个字典去存储该银行系统的账户信息,  卡号作为key --- user用户作为value
    def __init__(self,alluser):
        self.allUser = alluser

    # 开户
    def createUser(self):
        # 输入名字
        name = input("请输入您的名字:")
        # 输入身份证号
        idNumber = input("请输入您的身份证号:")
        # 输入用户手机号
        phone = input("请输入您的手机号:")
        # 验证, 数据格式的合法性(正则表达式),数据是否正确

        # 系统随机生成一个卡号(唯一的,不能与系统中的其他卡号重复)
        cardNumber = self.createCardNumber()
        # 设置密码(新密码需要输入两次(不一样需要重新设置))
        resPasswd = self.setPasswd()
        if resPasswd == -1: #如果设置密码时返回的是 -1 表示是一个恶意行为,则终止开户
            return  -1
        # 设置余额
        money = input("请输入您的金额:")
        # 判断 money需要大于 0
        # 创建一个card对象
        card = Card(cardNumber,resPasswd,money)
        # 创建一个user对象
        user = User(name,idNumber,phone,card)
        # 把用户存到alluser中, 卡号作为key,用户作为value
        self.allUser[cardNumber] = user
    #   测试
        print(self.allUser)

    # 设置密码
    def setPasswd(self):
        for i in range(3):
            passwd1 = input("你输入您的新密码:")
            passwd2 = input("请确认您设置的密码:")
            if passwd1 == passwd2: #设置密码成功
                return  passwd1
    #   此时,就表示3次设置都失败
        return -1





    #生成一个随机卡号
    def createCardNumber(self):
#       666 666    0-9     0078 23
        while True:
            cardNumber = ""
            for i in range(0,6):
                cardNumber += str(random.randrange(0,10))
            # 检测该卡号是否已经存在
            if not cardNumber in self.allUser: #卡号是否不存在
                return  cardNumber
        # print(cardNumber)

#   查询
    def queryMoney(self):
        #   请输入您的卡号
        cardNumber = input("请输入您要查询的卡号:")
        #  找到user
        #  找到卡,
        # 在alluser中查到对应的卡
        user = self.allUser.get(cardNumber)
        if user == None:
            # 作业: 可以输入3次卡号,超过3次,退出
            print("您输入的卡号不存在")
            return -1
        # 判断该卡是否已经被锁定
        if user.card.lock == True:#锁定
            print("此卡已经被锁定,无法查询该卡")
            return -1

        #   输入密码(输入错误,则可以重新输入3次,超过次数,就锁定该卡)
        passwd = input("请输入您的密码:")
        res = self.checkPasswd(passwd,user)
        if res == -1: #输入的密码多次错误,因该锁定该卡,并退出该功能
            # 锁起来
            user.card.lock = True
            return -1

        # 查询数据
        print("cardNumber:%s,money:%s"%(cardNumber,user.card.money))
        # pass

    # 用来检测密码是否正确
    def checkPasswd(self,passwd,user):
        for i in range(3):
            if passwd == user.card.passwd: #表示密码匹配成功:
                return 1
            # 走到这一步,表示最后一次也没有匹配成功
            if i == 2:
                return -1
#           匹配失败
            passwd = input("您的密码错误,请重新输入:")



#   存款
    def saveMoney(self):
        pass
#   取款
    def getMoney(self):
        pass
#   转账
    def  translateMoney(self):
        pass
#   改密
    def editPasswd(self):
        pass
#   锁定
    def lockCard(self):
        pass
#   解锁
    def unlockCard(self):
        pass
    # 补卡
    def fillCard(self):
        pass
#    注销
    def killCard(self):
        pass


