import os

#获取目录下的所有的目录名和文件名
def getAllDirAndFile(sourcePath):
    # 获取该目录下所有的文件目录名
    listFileName = os.listdir(sourcePath)
    for fileName in listFileName:
        # 拼接成完整的目录名
        absPath = os.path.join(sourcePath,fileName)
        # 判断是否是目录
        if os.path.isdir(absPath): #是目录
            print("目录:%s"%(fileName))
        #   需要继续查找
            getAllDirAndFile(absPath)
        #判断是否是文件
        if os.path.isfile(absPath): #是文件
            print("文件:%s"%(fileName))


# path = r"E:\pythondemo\bj1707"
path = r"I:\bj1707"
getAllDirAndFile(path)



















