'''
number数字:python中可以处理任意大小的数字,包括负数,小数,复数,处理时跟数学类似
number数字类型: 整型, 浮点,复数
'''
'''
# 数字
# 定义
num = 100
#赋值多个值
num1 = num2 = num3 = num4 = 20
num7 = num1

# python还支持交互式赋值
num5,num6  = 5,6
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
print(num7)
# 判断数据类型, int 就表示的是数字类型 , str表示字符串类型
print(type(num7))

print(type("100"))
# 获取内存地址
print(id(num1))
print(id(num2))
print(id(num))

num8 = 45
num9 = 45

print(id(num8))
print(id(num9))


# 浮点数字
# f1 = 1.1
# f2 = 2.2
f1 = 1.2
f2 = 1.3
f3 = f1 + f2
print(f3)
print(type(f3))

# 复数
'''

# 数据的转换
#  整数, 浮点数,字符串 之间转换
# 转换成整型
numm = 1.9
print(int(numm)) #会吧小数位舍掉
# print(int("123abc"))  #有其他非数字字符时会报错
print(int("+123")) #在数字字符前面有 + ,_表示正负的符号时可行
print(int("123"))

# 把其他类型转换成浮点型
numm1 = 89
print(float(numm1))

print(float("23.33"))

#把其他类型转换成字符串
s1 = str(23)
print(type(s1))



# 数据的处理
# 获取几个数字中的最大的数
maxNum = max(3,1,7,89,23,13,45)
print(maxNum)
#获取最小值
minNum = min(3, 1, 7, 89, 23, 13, 45)
print(minNum)

#数据的平方
print(pow(3,3))

# 求数据的绝对值
print(abs(-9))

# 四舍五入操作, round可以传入两个参数,第一个参数是需要四舍五入的值, 第二个参数是保留的小数位数(改参数可以舍弃,若舍弃默认不保留小数位)
print(round(3.1415926))
print(round(3.1415926,2))
print(round(3.1415926,3))























