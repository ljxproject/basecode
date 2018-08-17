# file = open('情书4.txt',"w",encoding="utf-8")
# file = open('情书5.txt',"w",encoding="utf-8")
file = open('情书5.txt',"a",encoding="utf-8")

# 写入一个字符串
file.write("其实我也暗恋你好久了,\n")
# file.write("滚吧,我耍你的")


# 写入一部分内容后,需要刷新缓存去
# 直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区写入 f.flush()
file.flush()

file.close()













