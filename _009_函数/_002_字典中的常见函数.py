
dic={"name":"张三","age":33}
# len() 获取字典中键值对个数
print(dic.__len__())

# keys 获取键列表
for i in dic.keys():
    print(i)

# values 获取值列表
for i in dic.values():
    print(i)

# 或取字典中元素以元组形式返回
for i in dic.items():
    print("%s,%s"%i)

# 判断key 是否在字典中  in
if "name" in dic:
    print(True)

