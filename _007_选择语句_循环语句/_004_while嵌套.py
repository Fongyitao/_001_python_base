#打印一个矩形

wide=int(input("请输入矩形宽:"))
high=int(input("请输入矩形高:"))

x=1
y=1
while y <= high:
    while x <= wide:
        print("*",end="")
        x += 1
    y+=1
    x=1
    print()
print('END')