#字符的编码和解码
# 向文件里写入编码后的字符
# with open("新闻.txt","wb") as wf:
#     news = "10月18日，中国共产党第十九次全国代表大会在北京人民大会堂隆重开幕。习近平代表第十八届中央委员会向大会作报告。"
# #   进行编码, 参数可以指定编码方式
#     bnews = news.encode(encoding="utf-8")
#     print(bnews)
#     # 写
#     wf.write(bnews)
#     wf.flush()

# 读二进制数据
with open("新闻.txt","rb") as rf:
    content = rf.read()
    # 解码
    news = content.decode(encoding="utf-8")
    print(news)































