# python的转意字符

# \n 表示换行符号
name = "wen"
age = 18
heigth = 1.888888

# print("name=%s,age=%d,heigth=%.3f"%(name,age,heigth))
print("name=%s\nage=%d\nheigth=%.3f"%(name,age,heigth))

print("""
鹅鹅鹅
曲线向天歌
包毛湖绿水
""")

#  \
str1 =  "money\\day"
# str2 =  "money\ay"  不建议这样写
print(str1)
# print(str2)

#  \"    \'
str3 = "wen is \"handsome\" man"
str5 = "wen is 'handsome' man"
str4 = 'wen is "handsome" man'
str6 = 'wen is \'handsome\' man'
print(str3)
print(str4)
print(str5)
print(str6)

# \t  tab制表符
str7 = "wen is\thandsome man"
print(str7)


# windows操作系统
# 路径格式: C:\Program Files (x86)\Baidu\BaiduPinyin\UIFrame
#linux
# 路径格式:  /baidu/wangpan


# 用文件路径时,需要转意
print("C:\\Program Files (x86)\\Baidu\\BaiduPinyin\\UIFrame")
# 当一个字符串需要大量的转意字符时, 可以在字符串前面加一个  r ,表示字符串中的转意字符不起作用
print(r"C:\Program Files (x86)\Baidu\BaiduPinyin\UIFrame")

print(r"\n")










































