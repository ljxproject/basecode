

def check():
    print("模拟的扩展功能")

def outter(func):
    def inner(*args,**kwargs):
        check()
        return func(*args,**kwargs)
    return inner

@outter
def func1(name,age):
    print("name:%s,age:%d"%(name,age))


# func1("金三胖胖",40)
# func1("金三胖胖",age = 80)
func1("金三胖胖",age = 80)





