# 全局变量的使用
num1 = 100

def func():
    # 告诉函数该变量时全局变量
    global num1
    print(num1)
    # num1 = 250
    print(num1)

func()
print(num1)





















