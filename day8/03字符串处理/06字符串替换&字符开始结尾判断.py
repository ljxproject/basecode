# 字符串的替换
str1 = "wen is good man!!  wen is a very  good man!! wen is a very  good man!! wen is a very  good man!! wen is a very  good man!! wen is a very  good man!! "
# 格式:  string.replace(old,new[,count])   old需要被替换的的字符, new用于替换的字符   count  替换多少个
# count 默认是全部替换(默认值是 -1),  有值时是表示从左到右需要替换的个数
# str2 = str1.replace("wen","xxx")
str2 = str1.replace("wen","xxx",2)
# str2 = str1.replace("wen","xxx",-1)
print(str2)














