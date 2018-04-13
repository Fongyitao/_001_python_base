import math

# 不带参数的函数
def print_hello():# 定义函数
    print("Hello")

print_hello()# 调用函数

# 带参数的函数
def circle_area(r):# 计算并返回圆的面积
    area=math.pi*r**2
    return area # 返回值，并结束函数

#计算半径为2的圆的面积
area=circle_area(2)
print("%f"%area)
print(area)


# 完善circle_area函数
def circle_area2(r):
    if not isinstance(r,(int,float)):
        print("传入的半径不是一个数字类型")
    else:
        return math.pi*r**2

print(circle_area2("2"))

