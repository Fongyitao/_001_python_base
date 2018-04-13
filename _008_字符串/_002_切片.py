a="abcdefghijklmnopqrstuvwxyz"

'''
切片是指对操作的对象截取其中一部分的操作,字符串/列表/元组都支持切片操作
切片语法:[起始:结束:步长]
注意:选取的区间数据左闭右开型,即不包含结束位本身.

'''

print(a[1:-1:2])# bdfhjlnprtvx
print(a[1::2])  # bdfhjlnprtvxz

# 逆序输出
b=a[::-1]
c=a[-1::-1]
print(b)
print(c)
# 也可以用循环实现
i=len(a)-1
while i>=0:
    print(a[i],end="")
    i-=1
print("----------")

# find查找
print(a.find("def"))#3
print(a.rfind("def"))

print(a.index("def"))
print(a.rindex("def"))


'''
count 出现次数

replace
把str1替换成str2,如果count指定,则替换次数不超过count次
my_str(str1,str2,my_str.count(str1))

split
以str为分隔符切片my_str,如果maxsplit有指定值,则仅分隔maxsplit个子字符串
my_str.split(str=" ",2)

'''

print("=====================")
my_str="Hello World 你好 世界 World おはようございます World"
print(my_str.split(" "))
print(my_str.split(" ",1))
print(my_str.partition("World"))# 截取,会保留截取字符串


print("=====================")
# capitalize 把字符串的一个字符大写
# title 把字符串的每个单子首字母大写

my_str1="abc def ghi"
print(my_str1.title())
print(my_str1.capitalize())


# endwit以xx字符串结尾
# statwith以xx字符串开头

# ljust   返回一个源字符串左对齐,并使用空格填充至长度width的新字符串
# rjust  返回一个原字符串有对齐,并使用空格填充至长度width的新字符串
# center 返回一个字符串居中对齐,并使用空格填充至长度width的新字符串
# my_str.ljust(witdth)

# strip 去除左右两边空白字符
# lstrip 删除字符串左边空白字符
# rstrip 删除字符串末尾的空白字符

# splitlines  按照换行符分隔,返回一个包含各行作为元素的列表

# isalpha 若my_str所有字符都是字母,则返回True,否则返回False
# isdigit 判断是否为数字,返回True或者False
# isalnum 判断是否是字母或者数字,返回True或者False

# join my_str中的每个字符后面插入list的每个元素后面,构造出一个新的字符串
names=["2018","03","27"]
print("-".join(names))# 2018-03-27

