name="abcdefg"
print(name[0])

print(name[len(name) - 1])
print(name[-1])

str = "hello world itcast and itxxx"
index = str.find("world")
print(index)  # 6 下标为6

index = str.find("dog")
print(index)  # -1  没有就返回 -1

index = str.rfind("itcast")
print(index)  # 12

index = str.index("w")
print(index)  # 6

count = str.count("o")
print(count)  # 2次

str1 = str.replace("it", "IT")  # 原字符串并未发生改变
print(str1)  # hello world ITcast and ITxxx
print(str)  # hello world itcast and itxxx

str2 = str.split(" ")  # 将字符串，按空格切割，返回一个列表，切割完之后，返回的列表里面就不在有空格了
print(str2)  # ['hello', 'world', 'itcast', 'and', 'itxxx']

str3 = str.capitalize()  # 将字符串的第一个字母大写
print(str3)  # Hello world itcast and itxxx

str4 = str.title()  # 所有单词的首字母大写
print(str4)  # Hello World Itcast And Itxxx

startwith = str.startswith("hello")
print(startwith)  # True

endwith = str.endswith("xxx")
print(endwith)  # True

str5 = str.lower()  # 全部转换为小写字母
print(str5)  # hello world itcast and itxxx
str6 = str.upper()  # 全部转换为大写字母
print(str6)  # HELLO WORLD ITCAST AND ITXXX

str7 = "Hello World"
str7 = str7.center(30)  # 居中p
print(str7)  # Hello World

str8 = str7.strip()  # 去除左右两边的空格
print(str8)  # Hello World

str9 = str.partition("it")  # 返回元组
print(str9)  # ('hello world ', 'it', 'cast and itxxx')

str10 = str.rpartition("it")
print(str10)  # ('hello world itcast and ', 'it', 'xxx')

str11 = str.splitlines()  # 按换行符切割，返回列表

str12 = "hello"
alpha = str12.isalpha()  # 判断一个字符串是否是 纯字母
print(alpha)  # True

digit = str12.isdigit()  # 判断一个字符串是否是 纯数字
print(digit)  # False

str13 = ["aaa", "bbb", "ccc"]
str14 = "--".join(str13)  # 把列表元素连接起来
print(str14)  # aaa--bbb--ccc