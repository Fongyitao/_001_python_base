class Person:
    def __init__(self):
        self.name="张三"
        self.age=23
        print("对象初始化")

    def work(self):
        pass

p1=Person() # 对象初始化
print(p1.name,p1.age)

print("---------------------")

class Student():
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def __init__(self):

        pass

    def introduce(self):
        print("姓名：%s,年龄：%s岁,身高：%sCM,体重：%sKG"%(self.name,self.age,self.height,self.weight))

# s1=Student("张三",23,165,60)
# s1.introduce()  # 姓名：张三,年龄：23岁,身高：165CM,体重：60KG

s2=Student()
s2.name="李四"
s2.age=24
s2.height=160
s2.weight=53
s2.introduce() # 姓名：李四,年龄：24岁,身高：160CM,体重：53KG
'''
若是在__init__中定义了形参，那么初始化对象的时候必须赋值,不然会抛异常
s2=Student()
TypeError: __init__() missing 4 required positional arguments: 'name', 'age', 'height', and 'weight'

当然，也可以再定义一个无参的__init__方法
__init__其实就是构造函数了

'''



