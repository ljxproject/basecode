#    "      标题       "
#  "左对齐      "
#  "              右对齐"
str1 = "wen is a good man"
# print(str1)
# 让字符串在某个宽度范围内居中
# 参数1: 宽度
# 参数2: 空白出填充的字符,  默认是空格
# str2 = str1.center(60)
str2 = str1.center(60,"*")
print(str2)


# 左对齐
str3 = "wen is a good man"
# str4 = str3.ljust(60)
str4 = str3.ljust(60,"*")
print(str4)

# 右对齐
str5 = "wen is a good man"
str7 = "man"
# str6 = str5.rjust(60)
str6 = str5.rjust(60,"*")

print(str6)
print(str7.rjust(60))













