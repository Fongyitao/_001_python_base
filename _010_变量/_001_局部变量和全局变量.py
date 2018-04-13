def sum(r):# 若函数中的局部变量和全局变量的变量名一样，那么优先使用局部变量
    pi=3.14 # 局部变量
    return (pi*2*r)

r=input("请输入半径：") # 全局变量
if r.isdigit():
    print(sum(float(r)))
else:
    print("输入有误")

