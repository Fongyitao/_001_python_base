# 自己调用自己

# 举例，计算阶乘
# n!=1*2*3*...*n
result=1
def factorial(n):
    global result
    if n > 0:
        for i in range(1,n+1):
            result *= i
        return result

print(factorial(9))

# 递归实现

def factorial2(n):
    if n == 1:
        return 1
    elif n > 1:
        return n*factorial2(n-1)

print(factorial2(9))