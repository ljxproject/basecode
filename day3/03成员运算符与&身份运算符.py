# 成员元算符
# in 表示一个值是否在一个数据集合中, 如果在则返回真,否则返回假
# not in 表示一个值是否在一个数据集合中, 如果不在则返回真,否则返回假

# class1706 = ["副院长","家属","精神病1","精神病2","精神病3"]
# if "副院长-患者" not in class1706:
#     print("True")
# else:
#     print("冒充者")

#身份运算符
# ==  表示2个变量的取值是否相同
# is 表示2个值的id(内存地址)地址是否是同一个值
# not is

num1 = 3
num2 = 3
num3 = [1,2,3]
num4 = [1,2,3]
num5 = num3

#
# if num1 is num2:
#     print("True")

if  num3 is num5:
    print("True")

print(id(num1))
print(id(num2))
print(id(num3))
print(id(num4))
print(id(num5))
























