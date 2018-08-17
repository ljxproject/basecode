'''
问题:
age1 = 50
age2 = 60
age3 = 70
age4 = 80
age5 = 90
age6 = 100

字典的方式存储数据
概述:是以 key - value的形式存储元素(键值对),具有极快的查找速度
     注意: key是无序的
     注意: key需要是不可变数据类型

key的特点:
    1,key是唯一的
    2.key需要是不可变数据类型
    3.字符串,数字等数据类型是不可变类型
    4.列表,字典是可变数据类型

# 创建一个字典
格式:    {key1:value1,key2:value2,.....}
描述:  字典的是以 { } 包裹起来的, 是以 key:value来表示一个元素,每个元素之间有  ,  连接
'''
# 创建一个空字典
dict1 ={}
print(type(dict1))

# 创建一个有多个元素的字典
dict2 = {"tom":23,"韩梅梅":89,"zhaoliu":34}
print(type(dict2))
print(dict2)

# key重复的字典, 如果key重复,会自动舍弃掉其他值,只保留一个
dict3 = {"tom":23,"韩梅梅":89,"zhaoliu":34,"tom":89,33:"34"}
print(dict3)


# 字典的增删改查
# 查
dict4 = {"tom":23,"韩梅梅":89,"zhaoliu":34,"yun":89,33:"34"}
# 字典不能用下标去访问元素
# print(dict4[0])
# 通过key来获取数据,  格式:   字典名[key]
# print(dict4["tom"])

# 注意:如果没有对应的key,程序会抛出异常
# print(dict4["tom2"])

# 通过get的方式访问元素, 如果该key不存在,则会返回空
age = dict4.get("tom2")
# print(age)
if age == None:
    print("该key不存在")
else:
    print("找到了该key")

# 设置默认值
age2 = dict4.get("tom2",20)
print(age2)

# 添加和修改
dict5 = {"tom":23,"韩梅梅":89,"zhaoliu":34,"yun":89,33:"34"}
# 添加
dict5["王五"] = 100
print(dict5)

# 修改
dict5["zhaoliu"] = 120
print(dict5)

# 格式  字典名[key] = 值
#     如果该key不存在,则表示的是添加一个新的元素
#     如果该key存在,则表示的是修改该key对应的值

# 删除
# 根据key来删除值 ,写法 :   字典名.pop(key)
dict6 = {"tom":23,"韩梅梅":89,"zhaoliu":34,"yun":89,33:"34"}
# dict6.pop("zhaoliu")
# 注意:  如果该key不存在,则程序会报错
# dict6.pop("zhaoliu2")
# print(dict6)

# 先判断该key是否存在于该字典中
if "zhaoliu2" in dict6:
    dict6.pop("zhaoliu2")


# 字典的遍历
# 直接遍历字典, 获取到的是每个元素的key
dict7 = {"tom":23,"韩梅梅":89,"zhaoliu":34,"yun":89,33:"34"}
# for key in dict7:
#     print(key,dict7[key])

# 获取字典所有的key后,在遍历
# print(dict7.keys())
# for key in dict7.keys():
#     print(key,dict7[key])

# 获取所有的value,
# print(dict7.values())
# for value in dict7.values():
#     print(value)


#将元素看成一个item,然后可以获取字典的所有item
# print(dict7.items())
# for key,value in dict7.items():
#     print(key,value)

for index,key in enumerate(dict7):
    # print(index,key)
    print(key, dict7[key])

# list与dict对比
'''
list
    在插入和查询速度上比较慢,随着元素个数的增加,会对查找速度产生过大的影响
    需求占用较小内存,内存浪费少

dict
    在插入和查询速度上比较快,随着元素个数的增加,不会对查找速度产生过大的影响
    需要占用较大内存 ,内存浪费多
'''


# 拷贝
dict8 = {"tom":23,"韩梅梅":89,"zhaoliu":34,"yun":89,33:"34"}
dict9 = dict8
dict8["tom"] = 130
print(dict8)
print(dict9)

dict10 = dict8.copy()
print(id(dict8))
print(id(dict10))


























































































































