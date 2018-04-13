def print_menu():
    print("="*30)
    print("名片管理系统V2.0".center(30))
    print('1、添加名片')
    print("2、查找名片")
    print("3、修改名片")
    print("4、删除名片")
    print("5、遍历名片")
    print("6、查看功能代码")
    print("q、退出")

def add_people():
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

def find_people():
    name = input("请输入要查找的名片：")
    for item in stus:
        if item["name"] == name.strip():
            print("姓名：%s，年龄为：%s,email为：%s" % (item["name"], item["age"], item["email"]))
            break
    else:
        print("%s名片不存在" % name)

def del_people():
    name=input("请输入要删除的名片：")
    for item in stus:
        if item["name"]==name.strip():
            stus.remove(item)
            print("删除成功")
            break
    else:
        print("名片不存在")


def show_people():
    print("序号\t姓名\t年龄\t邮箱")
    for i, item in enumerate(stus, 1):
        print("%s\t%s\t%s\t%s" % (i, item["name"], item["age"], item["email"]))

def start():
    print_menu()
    while True:
        operate = input("请输入功能代码：")
        if operate == "1":
            add_people()
        elif operate == "2":
            find_people()
        elif operate == "3":
            pass
        elif operate == "4":
            del_people()
        elif operate == "5":
            show_people()
        elif operate == "6":
            print_menu()
        elif operate == 'q':
            break

stus=[]# 存放名片信息
start()# 程序开始
