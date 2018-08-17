# 字符串的截取

wen = "wen is a nice man! 温"
# 截取字符串中的一个字符
# 字符串可以通过  字符串[字符索引] 来获取字符串中的一个字符,  位置从0开始
# str1 =  wen[0]
# print(str1)
# print(wen[-1])
# # len( 字符串) 表示获取字符串的长度
# # IndexError: string index out of range 角标越界异常,  表示超出了数据的长度范围
# # print(wen[len(wen)])
# print(wen[len(wen) - 1])
#
#
# # 截取一段字符
# # 格式:  字符串[start:stop]  截取start到stop范围内的字符串, 包前不包后
# str2 = wen[3:9]
# print(str2)
# # 表示截取某个位置以前的字符串
# str3 = wen[:8]
# print(str3)
# # 截取末尾的值
# str4 = wen[len(wen) - 4:]
# print(str4)
#
#
# # 逆向的截取
# # 索引前加上负号,表示倒着数
# str5 = wen[-4:]
# print(str5)

# str6 = wen[-1:-10] # 如果其实位置大于结束位置, 则截取不到
# print(str6)
# 格式  字符串[start:stop:step]  第三个参数表示步长(间隔几个字符后截取), 默认是 1
# str7 = wen[-1:-5:-1]
# print(str7)
#
#
# str8 = wen[-1::-2]
# print(str8)

str9 = wen[::]
print(str9)
































