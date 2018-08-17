""""
需求:  需要存储5个人的年龄,并计算平均值
age1 = 12
age2 = 13
age3 = 14
age4 = 15
age5 = 16
print((age1+ age2 + age3 +age4+age5)/5)

假设有100人,那么以上方法就不方便, 需要一个列表来存储多个数据
"""
# 列表的定义
# 定义一个空列表
list1 = []
# 定义一个有值的列表
# 可以存放多个数据,每个数据用 , 号隔开 ,
#元素可以重复
list2 = [2,3,8,12,78,12,34]
print(type(list1))
print(list2)

list3 = ["a","b","c"]
print(list3)
# 注意:可以存放多种类型
list4 = ["a","b","c",1,4,5]
print(list4)

# 获取列表中的一个元素
#可以通过下标索引来获取元素, (下标从0开始)
print(list4[0])
# 注意通过角标取值时,不要超过列表的长度
# print(list4[len(list4)])

# 例:
list5 = [2,3,8,12,78,12,34,12,34,12,34]
i = 0
count = 0
while i < len(list5):
    count += list5[i]
    i += 1
print(count/len(list5))

# 列表的常见操作
# 判断元素是否在列表中
if 78 in list5:
    print("存在")
else :
    print("buzai")

# 列表中的元素可以修改
# str1 = "wenjiabao"
# str1[0] = "h"  字符串的元素不能更改
list5[0] = 99
print(list5)

# 拼接
list6  = list5 + [90,12,33,34]
print(list5)
print(list6)

# *操作
list7 = list5 * 6
print(list7)

# 截取操作
# list8 =  list5[0:2]
# list8 =  list5[:2]
# list8 =  list5[2:]
list8 =  list5[::-1]
print(list8)

# 二维列表
list9 = [[12,34,12,23],[13,343,54,65],[134,341,125,236],[172,384,192,283]]
print(list9)
i = 0
while i < len(list9):
    # print(list9[i])
    j = 0
    while j < len(list9[i]):
        print(list9[i][j])
        j += 1
    i += 1






















































