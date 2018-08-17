#跳到某个位置
# file.seek(offset,from)
# 偏移的位置,(偏移多少个字节)
# from   0表示相对文件的起始位置,    1.表示相对当前位置     2.表示文件的结束位置
file = open("情书.txt","r",encoding="utf-8")
# content = file.read()
# print(content)
# 跳
file.seek(8,0)
# 获取当前位置
print(file.tell())

content = file.read()
print(content)



file.close()













