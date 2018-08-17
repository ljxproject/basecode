
# str1 = "****wen is a good man*****"
str1 = "****wen is a *** good man*****"
# str1 = "   wen is a good man    "
# 截取
# 参数: 表示需要去掉的 字符,  默认值是去掉空格
# 将字符中左侧的全部  参数表示的字符 去掉
# str2 = str1.lstrip("*")
str2 = str1.lstrip()
print(str2)

# 将字符中右侧的全部  参数表示的字符 去掉
str3 = str1.rstrip("*")
print(str3)


#左右两侧同时去掉
str5 = str1.strip("*")
print(str5)


















