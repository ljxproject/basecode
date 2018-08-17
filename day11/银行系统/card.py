# 银行卡类
class Card(object):
    def __init__(self,cardNumber,passwd,money=0):
        self.cardNumber = cardNumber  #银行卡卡号
        self.passwd = passwd  #银行卡密码
        self.money = money  #银行卡的余额
        self.lock = False  # 此属性表示该卡是否锁定, 默认是不锁定状态