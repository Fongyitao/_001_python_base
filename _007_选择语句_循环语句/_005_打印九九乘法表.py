
#while打印九九乘法表

i=1 # 行号
j=1 # 列号

while i<=9:
    while j<=i:
        print("%d x %d = %d"%(i,j,i*j),end="\t")
        j += 1
    i+=1
    j=1
    print()


