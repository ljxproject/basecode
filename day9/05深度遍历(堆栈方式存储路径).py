import os
# 深度遍历目录,获取该目录下的所有的目录名和文件名
def getAllDirAndFile(path):
    listDir = []
    listDir.append(path)

    while True:
        # 如果堆栈中没有了路径,则终止循环
        if len(listDir) == 0:
            break

    #   取出需要遍历的目录
        dealPath = listDir.pop()
        listFileName = os.listdir(dealPath)
        for  fileName in listFileName:
        #   拼接绝对路径
            absPath = os.path.join(dealPath,fileName)
            if os.path.isdir(absPath):
                print("目录:%s"%(fileName))
            #   添加到堆栈内存
                listDir.append(absPath)

            if os.path.isfile(absPath):
                print("文件:%s"%(fileName))


path = r"E:\pythondemo\bj1707"
# path = r"I:\bj1707"
getAllDirAndFile(path)












