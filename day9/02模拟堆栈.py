# 模拟堆栈
#  [1,2,3,4,5]  pop

stack = []
# 压栈  (存数据)
# 模拟存数据
stack.append("A")
print(stack)
# 继续存
stack.append("B")
print(stack)

stack.append("C")
print(stack)


# 取  出栈
# 删除 栈顶,并获取该值
# pop方法默认删除列表最后面的值, 并将删除的值作为返回值
res1 = stack.pop()
print(res1)
print(stack)

res2 = stack.pop()
print(res2)
print(stack)













































