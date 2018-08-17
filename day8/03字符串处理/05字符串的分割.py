# 字符串的分割
"23,we,yu,ui,ui"
str1 = "张三,李四,王五,赵六,龙骑,王八"
str2 = "wen is a good man"
# jiang该字符串进行以 参数传入的符号 分割, 分割的结果是分割后的多个字符串组成的列表
# res = str1.split(",")
# 默认情况以空格作为分隔符
res = str2.split()
print(res)
print(type(res))




str3 = """wen is a good man
wen is a nice man
wen is a handsome man
"""
#将字符串一行一行的进行切割
# res2 = str3.splitlines()
# 参数keepends 表示是否保留换行符, True 保留,   默认是False
res2 = str3.splitlines(True)
print(res2)
print(type(res2))


# 拼接字符串
# list1 = ["张三","李四","王五","赵六"]
list1 = ("张三","李四","王五","赵六")

#表示多个字符以  该字符 为分割符进行拼接
str6 = "***".join(list1)
print(str6)















