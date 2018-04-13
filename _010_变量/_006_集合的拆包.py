def test2(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)
    sum = x
    for i in args:
        sum += i
    for i in kwargs.values():
        sum +=i
    return sum


nums=[1,5,3,7]
nums2={"num1":1,"num2":5,"num3":7}

sum2 = test2(1,*nums,**nums2)# 拆包

print(sum2)

