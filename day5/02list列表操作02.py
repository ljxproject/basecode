# 增删改查
#添加
list1 = [90,89,78,68,23,45,67,89]
# 添加一个值,会将这个元素添加到原有list的末尾
list1.append(120)
print(list1)

# 添加多个元素
list2 = [34,56]
list1.extend(list2)
print(list1)

# 插入一个元素
#参数1 表示插入位置的角标
# 参数2  表示插入的值
# 将参数2插入到列表的的参数1位置,被替换的元素以及该位置后面的元素都会后移
list1.insert(2,222)
print(list1)

# 删除一个元素
list3 = [90,89,78,68,23,45,67,89]

# 参数: 表示需要删除的元素的位置
# 根据位置来从列表中删除元素,  参数可以不写,不写表示默认,默认删除列表的最后一个元素
# list3.pop()
# list3.pop(2)
# print(list3)

# 根据元素的值来删除, 删除第一个匹配的数
# list3.remove(68)
# list3.remove(89)
print(list3)

# 清除操作
list3.clear()
print(list3)

# 删除
# del list3
# print(list3)


# 修改
# python中只有 列表和字典是可变类型

list5 = [23,45,67,89,12,34,56]
# list中的元素可以直接 以 list[下标] = 值   的方式进行修改
list5[0] = 100
print(list5)


# 查找
# 获取列表中的元素
# 可以根据下标查找元素
list4 = [23,45,67,89,12,34,56]
# 角标是从0开始, 不能越界
age = list4[0]
# age = list4[7]
print(age)

# 根据元素的值来获取角标位置
print(list4.index(45))


# 访问列表的长度
list6 = [23,45,67,89,12,34,56,89]
print(len(list6))
# 统计一个元素在列表中出现的次数
# print(list6.count(89))
# 彻底删除一个值
for i in range(list6.count(89)):
    list6.remove(89)

print(list6)


list7 = [23,45,67,89,12,34,56,89]
# 可以给列表中的元素进行排序
# 表示从小到大排序
list7.sort()
# 降序
list7.sort(reverse=True)
print(list7)

# # 反转
# list7.reverse()
# print(list7)
#
#
# # 求最大值,最小值
# print(max(list7))
# print(min(list7))

#拷贝
list8 = [12,23,34,45]
list12 = [12,23,34,45]

list9 = list8
list9[0] = 100
print(list8)
print(list9)

print(id(list8))
print(id(list12))
print(id(list9))


# copy拷贝
list10 = [12,23,34,45]

list11 = list10.copy()
list11[0] = 100

print(list10)
print(list11)
print(id(list10))
print(id(list11))


age = 1
print(id(age))
age=2
print(id(age))
age2 = 1
print(id(age2))














































































