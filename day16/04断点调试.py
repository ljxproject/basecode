
def add(a,b):
    c = a + b
    return c

def divi(a,b):
    return a/b

def main():
    a = int(input("请输入数字:"))
    b = int(input("请输入第二个数字:"))
    c = add(a,b)
    d = divi(a,b)
    print(c)
    print(d)



if __name__ == '__main__':
    main()

