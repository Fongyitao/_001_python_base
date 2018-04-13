def test1(x,y,z=10):# 缺省参数需放在参数列表后面
    print(x,y,z)
    return x+y+z

print(test1(1,3,5))# 9
print(test1(1,3))# 14
