'''
文件的基本操作:
    1.打开一个文件,或者创建一个新文件
    2.文件的读/写操作
    3.关闭连接

1.打开一个文件
格式:

open(file[,mode][,encoding][,errors="igonre"])
file是要打开的文件路径
encoding文件编码-解码,   UTF-8,  gbk
errors="igonre"  忽略错误,可能会造成数据丢失
mode表示的是文件打开的模式, 默认模式是 r
r     表示以只读的形式打开,      文件定位符在文件的起始处,如果文件路劲不对,则会报文件找不到异常(FileNotFoundError),
rb    表示以二进制的读的方式打开,    文件的定位符在文件的起始处,如果文件路径不对,则出现文件找不到异常
r+    表示以读写的方式打开文件,    文件的定位符在文件的起始处,如果文件路径不对,则出现文件找不到异常
rb+   表示二进制读写的方式打开,

w     表示以只写的方式打开    文件的定位符在文件的起始位置,并且会将原有的文件内容擦除掉,如果文件不存在,会新建一个新的文件
wb    表示以二进制写的方式打开     文件的定位符在文件的起始位置,并且会将原有的文件内容擦除掉,如果文件不存在,会新建一个新的文件
w+    表示以读写的方式打开文件     文件的定位符在文件的起始位置,并且会将原有的文件内容擦除掉,如果文件不存在,会新建一个新的文件
wb+   表示以二进制读写的方式打开

a 追加,  表示以只写的方式打开     文件的定位符放在文件的末尾,不会擦除文件原本的内容,会在原文件内容后继续追加, 如果文件不存在,会创建一个新的文件
ab
a+
ab+
'''

# 打开文件
# file  = open("情书.txt")  #默认的解码方式是 gbk
# file = open("情书.txt",encoding="utf-8")
# 文件路径不能错误,
# file = open("情书2.txt",encoding="utf-8")

# 以二进制的形式打开, 注意不需要进行编码
# file = open("情书.txt","rb")

# 以只写的方式打开
# file = open("情书2.txt","w",encoding="utf-8",errors="ignore")
# file = open("情书3.txt","w",encoding="utf-8",errors="ignore")
# file = open("情书2.txt","w+",encoding="utf-8",errors="ignore")

# 以追加的方式打开
# file = open("情书2.txt","a",encoding="utf-8",errors="ignore")
# file = open("情书4.txt","a",encoding="utf-8",errors="ignore")

# 读文件
# 读取全部文件
# content = file.read()
# print(content)

# 关闭文件
# file.close()


#抛出异常
# try:
#     # 可能出现异常的代码
#     file = open("情书4.txt", "a", encoding="utf-8", errors="ignore")

# finally:
#     # 无论文件打开时是否出现异常,都需要关闭
#     if file != None:
#         file.close()

#精简方式
# 不需要close,自动关闭
with open("情书5.txt", "r", encoding="utf-8", errors="ignore") as file:
    print(file.read())










































