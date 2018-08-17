# 需求: 复制一个文件到相对目录下
# 思路:
#   1.输入一个源文件名
#   2.创建目标文件(打开)
#   3.打开源文件,进行读的操作,获取读的内容
#   4.将源文件的内容写入目标文件
#   5.关闭源文件,关闭目标文件

sourceFile = input("请输入需要复制的文件名:")
#  名字:   源文件名  .格式 -----> 源文件名[副本].格式
position = sourceFile.rfind(".")
# 拆分源文件
fileDir = sourceFile[:position]
filed =  sourceFile[position:]
print(fileDir)
print(filed)

# 拼接目标文件名
targetFileName = fileDir + "[副本]" + filed
# 打开目标文件
# targetFile = open(targetFileName,"w",encoding="utf-8")
targetFile = open(targetFileName,"wb")
# 打开源文件
# sourceF = open(sourceFile,"r",encoding="utf-8")
sourceF = open(sourceFile,"rb")
# 读
# content = sourceF.read()
# # 写到目标文件
# targetFile.write(content)
# targetFile.flush()

# 复制大文件
while True:
#    读  一次性读取1024字节   1M
    content = sourceF.read(1024)
    # 判断是否读取完毕
    if len(content) == 0:
    #     跳出循环
        break
    targetFile.write(content)
    targetFile.flush()

# 关闭文件
sourceF.close()
targetFile.close()




































