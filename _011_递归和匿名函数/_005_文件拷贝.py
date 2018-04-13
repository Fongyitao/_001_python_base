source_file="/Users/Fong/Downloads/bear.png"
dest_file="copy_"+source_file[source_file.rfind("/")+1:]
print("目标文件是：%s"%dest_file)

# 打开文件
source_f=open(source_file,mode="rb")

# 读取原始文件
content=source_f.read()

# 把读取到的内容写入到目标文件中
dest_f=open(dest_file,mode="wb")
dest_f.write(content)

source_f.close()
dest_f.close()

