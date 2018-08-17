str1 = "wen is good man88"
str2 = "Wen iS gOOd man99"
str3 = "Wen iS good man88"
str4 = "Wen  Is  Good Man88"

# 将字符串全部转换成大写
print(str1.upper())

# 将字符串全部转换成小写
print(str2.lower())

#让字符串的单词首字母大写
print(str2.title())

# 切换大小写
print(str4.swapcase())

# 让一串字符的首字母大写
print(str2.capitalize())

# 判断一个字符串是否是全部是大写,
# 如果该字符串中(至少有一个英文字符时)所有的英文字符是大写,则返回True
print("abc".isupper())
print("aBc".isupper())
print("ABC".isupper())
print("AB温C".isupper())
print("AB89".isupper())
print("89".isupper())

# 判断字符串中的字符是否是全小写
print("abc".islower())
print("abC".islower())
print("89".islower())
print("abc温".islower())

#判断是否是title,判断字符串中所有的单词的首字母是否大写
print("Wen Is A Good Man".istitle())
print("Wen Is A Good 温 Man".istitle())






















