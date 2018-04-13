names=["Ryan","Jack","Tom"]
stu={"name":"张三"}
a = "李四"

def test1():
    print("原始全局变量为：%s"%names)
    names[0]="Rose"
    stu["age"]=23
    global a # 不可变类型，要重新赋值需要在变量名前加global
    a="王五"

test1()

print("最后全局变量为：%s"%names)
print("最后全局变量为：%s"%stu)
print("最后全局变量为：%s"%a)

# 在函数中修改全局变量：1、如果是可变类型，可以执行修改；2、如果全局变量是不可变类型，需加global，本质是修改引用