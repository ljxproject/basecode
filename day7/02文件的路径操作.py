# 打开一个文件
# 相对路径,   文件在与该程序相同的目录下
# file = open("情书.txt", "r", encoding="utf-8", errors="ignore")
# 绝对路径     文件完整的路径

# path = "E:\\pythondemo\\bj1707\\hello.txt"
path = r"E:\pythondemo\bj1707\hello.txt"
file = open(path, "r", encoding="utf-8", errors="ignore")
content = file.read()
print(content)


file.close()







