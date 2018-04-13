def avg_3_num(a,b,c):
    if is_number(a) and is_number(b) and is_number(c):
        return (a+b+c)/3
    else:
        print("无法计算平均值")

def is_number(a):
    if not isinstance(a,(int,float)):
        print("所传参数%s不是一个数字类型"%a)
        return False
    else:
        return True

avg = avg_3_num(3,5,7)
print(avg)

# 整个程序执行顺序是：首先内存加载函数avg_3_num,但是函数里面的代码没有执行，因为没有调用，而后执行函数is_number，同样不执行里面代码，最后第14行代码调用了avg_3_num于是就执行了其中代码，再调用了is_number执行其中代码

