
def check():
    print("模拟的扩展功能")


def outter(func):
    def inner(name):
        check()
        func(name)
    return inner

# 在函数的上方加上@符号,@符号加上一个装饰器名,表示将该名字对应的装饰器应用在该函数上
# 本质:  相当于执行了     func1 = outter(func1)    跟函数名同名的一个装饰后的函数名 =  装饰器名(函数名)
@outter
def func1(name):
    print("基础功能1")
    print("名字是:%s"%(name))

# def func2():
#     print("基础功能2")

func1("金三胖胖")








