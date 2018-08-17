# 作用域: 变量可以使用的范围
# 程序的变量并不是在所有位置都能使用的，   访问的权限决定于变量的在哪里赋值的


# 在python中只有模块,类,函数 会引入新的作用域, python中 if,elif,while,for循环不会引入新的作用域

# def func():
#     num1 = 100
#     print(num1)
#
# func()
# 不能使用函数里定义的变量
# print(num1)

if False:
    num1 = 100
    print(100)

print(num1)














