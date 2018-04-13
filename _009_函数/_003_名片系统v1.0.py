msg = '''
功能代码如下：
====================
1：添加学生
2：查找学生
3：修改学生
4：删除学生
5：遍历学生
q：退出
====================
'''
print(msg)
stus = []  # 存储学生信息

while True:
    operate = input("请输入功能代码：")
    if operate == "1":
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        email = input("请输入邮箱：")
        # 将学生的三个信息存到字典中
        stu = {}
        stu["name"] = name
        stu["age"] = age
        stu["email"] = email
        stus.append(stu)
        print("添加成功")
    elif operate == "2":
        name = input("请输入要查找的姓名：")
        for item in stus:
            if item["name"] == name.strip():
                print("%s学生存在，年龄为：%s,email为：%s" % (item["name"], item["age"], item["email"]))
                break
        else:
            print("%s学生不存在" % name)

    elif operate == "3":
        pass
    elif operate == "4":
        pass
    elif operate == "5":
        print("序号\t姓名\t年龄\t邮箱")
        for i, item in enumerate(stus, 1):
            print("%s\t%s\t%s\t%s" % (i, item["name"], item["age"], item["email"]))

    elif operate == 'q':
        break
