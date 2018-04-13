'''
for 临时变量 in 列表或者字符串等:
    循环满足条件时执行的代码
else:
    循环不满足条件时执行的代码
'''

for i in "abcdefg":
    print(i,end="\t")
else:
    print("------没有内容-------")

for i in range(1,10):
    print(i,end="\t")
else:
    print("------没有内容-------")
