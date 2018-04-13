def test1(x,y,*args,z=10):
    print(x,y)
    print(args)
    sum=x+y+z
    for i in args:
        sum+=i
    return sum

sum1=test1(1,2,3,4,5,6,7,8,9,z=20)
print(sum1)

print("*"*10)
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

sum2 = test2(2,3,5,num1=1,num2=3,num3=5)
'''
2
(3, 5)
{'num1': 1, 'num2': 3, 'num3': 5}
'''
print(sum2)