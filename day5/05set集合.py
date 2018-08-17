'''
set集合:
与dict类似, 是一组key的集合, 没有value
本质:是无序,无重复元素的集合
'''
# 创建一个set集合
# 创建一个空的set集合
set1 = set()
# set1 = {23,34}  表示的是set类型
# set1 = {}     表示的是dict类型

print(set1)
print(type(set1))

# 创建有多个元素的集合,   需要将 列表或者字典或者元组或者字符串 传进set作为多个元素

#将列表转换成set
list1 = [12,23,34,45,12]
set2 = set(list1)
print(set2)
print(type(set2))
list2 = list(set2)
print(list2)
print(type(list2))

#将dict转换成set, 只转换字典的key
dict1 = {"tom":23,"韩梅梅":89,"zhaoliu":34,"yun":89,33:"34"}
set3 = set(dict1)
print(set3)
print(type(set3))

# 将元组转换成set
tuple1 = (12,23,34,56,12)
set4 = set(tuple1)
print(set4)

# 将String字符串转换成set
message = "wen is a good man"
set5 = set(message)
print(set5)

# 增删改查
# 查
# 遍历值
set6 = set([12,23,34,45,56,12,23])
# for key in set6:
#     print(key)
# for index,key in enumerate(set6):
#     print(index,key)

# 判断是否存在该key
if 56 in set6:
    print("存在")

# 不能直接修改

# 添加新的元素
# 添加一个元素, 如果该元素原本就在set中,则添加不进去
set7 = set([12,23,34,45,56,12,23])
print(set7)
# set7.add(78)
set7.add(12)
# set7.add((23,32,34))
print(set7)

# 添加多个元素(跟新), update方法需要传入一个存放多个元素的元组或者列表
# set8 = set([12,23,34,45,56,12,23])
# print(set8)
# set8.update((23,32,34))
# print(set8)

# 删除
set9 = set([12,23,34,45,56,12,23])
print(set9)
set9.remove(23)
print(set9)


# 交集  并集
set10 = set([12,23,34,45])
set11 = set([23,34,45,56,67,78])

# 交集
set12 = set10 & set11
print(set12)

# 并集
set13 = set10 | set11
print(set13)























































