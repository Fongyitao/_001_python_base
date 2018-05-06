import os

# 从temp目录找到.py结尾的文件，并且读取其中内容，看是否包含有"Hello"，返回其文件名

file_list=[] # 存放符合的文件

# 找文件的函数
def find_file(file_path):
    if os.path.isdir(file_path):
        for i in os.listdir(file_path):
            find_file(os.path.join(file_path,i))
    else:
        if file_path.endswith(".py"): # 如果传入的是文件，判断是否以.py结尾
            if read_find_file(file_path): # 读取文件内容，看内容中是否包含"Hello"
                print(file_path)
                file_list.append(file_path)

# 读取文件内容的函数
def read_find_file(py_file):
    flag=False
    '''
    f=open(py_file,"r")
    while True:
        line=f.readline()
        if line=="": # 文件读到最后一行，终止循环
            break
        elif "Hello" in line:
            flag=True
            break
    f.close()
    '''

    with open(py_file,"r") as f:
        while True:
            line=f.readline()
            if len(line)==0:
                break
            elif "Hello" in line:
                flag=True
                break

    return flag

file_path="/Users/Fong/temp"
find_file(file_path)
print(file_list)


