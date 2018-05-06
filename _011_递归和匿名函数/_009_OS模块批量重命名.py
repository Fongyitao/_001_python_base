import os

# 给文件批量重命名
file_path="/Users/Fong/temp/"

file_list=os.listdir(file_path)

for f in file_list:
    print(f)

    # dest_file="rename"+f # 重命名后的文件名 # 想在rename后面加 '-'

    source_file = os.path.join(file_path,f)

    # parent_dir = os.path.join(file_path,dest_file)
    # os.rename(os.path.join(file_path,f),os.path.join(file_path,dest_file))

    re_dest_file = "-".join([f[:6], f[6:]])
    parent_dir = os.path.join(file_path,re_dest_file)

    os.rename(source_file,parent_dir)

