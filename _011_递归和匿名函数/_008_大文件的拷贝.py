old_file_name=input("请输入需要拷贝的文件名：")

position=old_file_name.rfind(".")

new_file_name="-副本".join([old_file_name[:position],old_file_name[position:]])

with open(old_file_name,"rb") as old_file,open(new_file_name,"wb") as new_file:
    while True:
        data=old_file.read(1024*5)
        if len(data)==0:
            break
        new_file.write(data)

