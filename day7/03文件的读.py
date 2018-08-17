file = open("情书.txt","r",encoding="utf-8")
# file = open("情书.txt","rb")
# 如果读取的是二进制数据，则 参数表示的是读取多少个  字节
# 汉字在utf-8中占3个字节长度， 在gbk中占据2个字节长度
# content = file.read(12)
# # 解码
# print(content.decode("utf-8"))


# 读取
# 读取全部内容
# content = file.read()
# print(content)

# 读取部分内容,
# read参数 表示读取多少个字符（汉字也算一个字符）
# content = file.read(6)
# print(content)

#
# # 注意： 继续读时，会从上次读的位置继续读
# content2 = file.read(6)
# print(content2)

# 一行一行的读取数据
# line = file.readline()
# print(line)
# print(file.readline())

# 一次性读取多行
# lines = file.readlines()
# # print(lines)
# # print(type(lines))
# for line in  lines:
#     print(line)


















file.close()
















