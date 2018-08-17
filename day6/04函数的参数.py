# 需求: 定义一个有参数的函数 ,     打印一个人的姓名和年龄
# 在函数定义的时候()里的参数叫形式参数,用来接收函数调用的实际参数
# 调用函数时相当于执行了    name(形式参数)  = "张三"(实际参数)     age = 90
def printNameAndAge(name,age):
    # print(name)
    print("name=%s,age=%d"%(name,age))

# 调用
# 在函数调用时传入的参数叫实际参数
# printNameAndAge("张三",90)
# name = "金三胖胖"
# age = 30
# printNameAndAge(name,age)

# 调用函数传递参数的顺序需要与定义的函数参数顺序一致
# printNameAndAge(67,"习大大")

#传入实际参数的个数需要与定义时个数一致
# printNameAndAge("习大大")




















