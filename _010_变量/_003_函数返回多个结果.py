def test1():
    a=1
    b=2
    return a,b

x=test1()
print(x)# (1, 2)

x,y=test1()
print(x)# 1
print(y)# 2

