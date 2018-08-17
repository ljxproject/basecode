# 在字符串中查找某个字符串的位置
# find - rfind
str1 = "wen is a very very good man"
# 在字符串中查找某个字符串第一次出现的位置(下标), 如果没有找到对应的字符串会返回-1
# position1 = str1.find("wen")
position1 = str1.find("veryyyy")
print(position1)

# 从字符串的右侧开始找,会找到第一个匹配项的位置
position2 = str1.rfind("very")
print(position2)

#参数1:sub查找的字符串   参数2:start=None查找的范围的起始位置  参数3end=None结束位置
# 参数2,和参数3不写时表示在整个字符串范围查找
position3 = str1.rfind("very",8,15)
print(position3)

# index 查找,  与find查找类似,  如果查找的字符串在原字符串中没有找到则会报错
str2= "wen is a very very good man"
# posi4 = str2.index("wen")
# posi4 = str2.index("very")
# 从右侧开始找,找到第一个匹配上的位置
posi4 = str2.rindex("very")
# posi4 = str2.index("veryyyy")

print(posi4)


















