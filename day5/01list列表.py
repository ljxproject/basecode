'''
问题:
age1 = 20
age2 = 30
age3 = 40
age4 = 50
age5 = 60
age6 = 70
处理:  print((age1 + age2 + age3 + age4 + age5 + age6)/6)
假设有100个值

list列表,  可以用来存储多个数据

格式: 列表是以[] 包裹的内容,[]中可以存放多个元素,每个元素用  ,  隔开 ,列表中的元素可以是不同的类型

'''
# 创建一个list列表
# 创建一个空的列表
list1 = []
print(type(list1))
print(id(list1))


# 创建一个有元素的列表
list2 = [23,45,67,89,12,34,56]
print(list2)


#注意: 列表中的元素可以是不同的类型
list3 = ["2","wen","hello",12,45,67]
print(list3)


# 获取列表中的元素
# 可以根据下标,
list4 = [23,45,67,89,12,34,56]
# 角标是从0开始, 不能越界
age = list4[0]
# age = list4[7]
print(age)



count = 0
# 求平均值
for i in range(len(list4)):
    # print(list4[i])
    count += list4[i]

print(count/len(list4))


# 修改
# String是不可变类型,不可以修改
messag = "wen is a good man"
# print(messag[0])
# messag[0] = "Q"

# python中只有 列表和字典是可变类型

list5 = [23,45,67,89,12,34,56]
# list中的元素可以直接 以 list[下标] = 值   的方式进行修改
list5[0] = 100
print(list5)

# 列表的常见操作
# + 拼接操作
list6 = [12,34,56,12,34,56]
list7 = [90,89,78,68]
list8 = list6 +  list7
print(list8)

# *  操作,  一个列表可以存放相同的元素
list9 = [90,89,78,68]
list10 = list9 * 12
print(list10)


# 判断元素是否在列表中
if 68 in list10:
    print("存在")

# 列表的截取
list12 = [90,89,78,68,23,45,67,89]
print(list12[-1])
print(list12[0:3])
print(list12[:3])
print(list12[::-1])



# # 二维列表,列表中存放列表
# list11 = [[12,13,14,15],[23,24,25,26],[33,34,35,36]]
# # 获取二维列表中的一个元素
# print(list11[0])
# #获取子元素
# print(list11[1][3])
# # 三维列表

messag = "wen is a good man"
print(messag[4:6])
















































































