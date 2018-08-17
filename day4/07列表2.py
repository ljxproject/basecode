# 列表的操作
# 增加
list1 = [2,3,8,12,78]
list2 = list1 + [23,16]
print(list2)
#append 表示向列表中添加一个元素,会添加到列表的末尾
list1.append(99)
print(list1)
# extend 表示向列表中添加一个列表,会将列表的数据添加在原数据的末尾
list1.extend([88,77])
print(list1)
# 插入,想列表的某个位置插入一个元素, 前面的元素不变,后面的元素后移
list1.insert(2,2222)
print(list1)

# 删除操作
list3 =  [2,3,8,12,3,78]
# pop表示删除一个元素,默认删除最后一个
# list3.pop()
#根据下标索引去删除数据
# list3.pop(3)
print(list3)

#remove(m) 表示移除列表中第一个匹配的m 元素
list3.remove(3)
print(list3)

# 清空列表中的数据
list3.clear()
print(list3)

# 删除
# del list3
# print(list3)

# 查
list4 =  [2,3,8,12,3,78]
#根据索引来查数据
print(list4[2])
# 根据元素的值来查找该值在列表中的第一次出现的位置
index = list4.index(3)
print(index)


# 改
# 列表中的元素可以修改
# str1 = "wenjiabao"
# str1[0] = "h"  字符串的元素不能更改
# list5[0] = 99
# print(list5)


list6 =  [2,3,8,12,3,78]
# 取最大值
maxAge = max(list6)
print(maxAge)
# 取最小值
minAge = min(list6)
print(minAge)

# 排序
list7 =  [2,56,3,23,8,12,3,78]
# 从小到大
list7.sort()
print(list7)
# 逆序
list7.reverse()
print(list7)

# 统计某个元素值出现的次数
list8 =  [2,56,3,23,8,12,3,78]
count = list8.count(3)
print(count)
i = 0
while i < list8.count(3):
    list8.remove(3)
print(list8)

# 列表的拷贝
list9 =  [1,2,3,4,5,6,7,8]
list10 = list9
list10[0] = 99
print(list9)
print(list10)

# 拷贝
list11 =  [1,2,3,4,5,6,7,8]
list12 = list11.copy()
list12[0] = 99
print(list11)
print(list12)



























































