# list是一种有序的集合,可以随时添加和删除其中的元素

names=["Alice","Jack","Tom","Tracy"]
print(names[1])

# 添加元素
# append,extend,insert

# append是在列表的末尾追加
names.append("Ryan")
print(names)

# extend 可以将一个列表中的元素追加到另一个列表末尾
names2=["张三","李四"]
names.extend(names2)
print(names)

# insert 在指定下标位置插入元素
names.insert(0,"Bob")
print(names)

# 修改元素
# 通过下标重新给元素赋值
names[1]="Alen"
print(names)

# 查找元素
# in , not in
# in(存在),如果存在结果为True,否则为False
# not in(不存在),如果不存在结果为True,否则为False

print("Bob" in names) # True

# count 元素个数
num = names.count("Alice")
print(num)

# 删除元素
# del,pop,remove
# del 根据下标进行删除,其实可以删除所有变量
# pop 默认删除最后一个元素,并且把这个元素个返回
# remove 根据元素的值进行删除第一个

print(names.pop(0))# Bob
del names[0]
names.remove("张三")

# 排序,逆置
# sort reverse

# sort默认是升序,可以改参数reverse为True就为降序

numbers=[2,1,5,3]
numbers.sort(reverse=True)
print(numbers)

