import os
# 指定相对目录
# file = open("情书.txt", "r", encoding="utf-8", errors="ignore")
# file = open(r"新闻\情书.txt", "r", encoding="utf-8", errors="ignore")
# content = file.read()
# print(content)
# file.close()

# 指定绝对路径
# path = "E:\\pythondemo\\bj1707\\hello.txt"
# path = r"E:\pythondemo\bj1707\hello.txt"
# file = open(path, "r", encoding="utf-8", errors="ignore")

# 目录的操作
# 获取当前的目录  . 表达当前目录,    .. 上一级目录
# print(os.curdir)
# file = open(r"..\hello.txt", "r", encoding="utf-8", errors="ignore")
# content = file.read()
# print(content)
# file.close()

# 获取当前工作目录
# path = os.getcwd()
# print(path)

# 获取当前目录下的所有文件的文件名(包括目录)
# 空参数表示获取当前目录下的所有文件名(包括目录)
# 可以传入绝对路径
# fileNames = os.listdir()
# fileNames = os.listdir(r"I:\bj1707\day06\code")
# print(fileNames)
# print(type(fileNames))

# 在当前目录下创建一个目录,
# 注意:如果该文件已经存在,则会报异常
# os.mkdir("十九大")
#在绝对路径下创建一个目录
# os.mkdir(r"I:\bj1707\hello")
# 以下方式创建的任然是目录
# os.mkdir(r"I:\bj1707\yyy.txt")

# 可以修改目录,文件名名
# 参数1 表示修改前的名字,   参数2:修改后的名字
# 修改文件名
# os.rename("情书5.txt","情书xxxxx.txt")
# 修改目录名
# os.rename("新闻","习大大")
# 传递绝对路径
# os.rename(r"I:\bj1707\yyy.txt",r"I:\bj1707\yyy")

# 删除
# 删除目录
# os.rmdir("十九大")
# 删除文件
# os.remove("情书xxxxx.txt")

# 获取文件的属性
# print(os.stat("情书.txt"))


# 获取文件的绝对路径
# print(os.path.abspath("情书.txt"))

# 路径的拼接
# path1 = r"I:\bj1707"
# fileName = r"\tupian.png"
# filePath =  path1 + fileName
# print(filePath)

# 拼接路径
# absPath = os.path.join(os.getcwd(),"hahaha.txt")
# file =open(absPath,"w")
# file.close()

# 分割路径,会分割成元组的形式,  元组第一个参数是, 该文件目录路径 ,参数2: 文件名
# path1 =  r"I:\bj1707\day06\code\01list列表.py"
# path2 =  r"01list列表.py"
# print(os.path.split(path1))
# # print(os.path.splitext(path1))
# # 分割文件名与该文件名的格式
# print(os.path.splitext(path2))

# 判断是否是目录
path1 =  r"I:\bj1707\day06\code\01list列表.py"
path2 =  r"I:\bj1707\day06\code"
# isDir1 = os.path.isdir(path1)
isDir1 = os.path.isdir(path2)
print(isDir1)
# 判断是否是文件
isFile = os.path.isfile(path1)
print(isFile)

#判断该目录,文件是否存在
print(os.path.exists(path1))
print(os.path.exists(path2))

# 获取文件的路径的目录
print(os.path.dirname(path1))
print(os.path.basename(path1))

#shell命令
# os.system("notepad")
os.system("write")






















































