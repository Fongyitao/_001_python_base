'''
定位到某个位置：
在读写文件的过程中，需要从另一个位置进行操作的话，可以使用seek()
seek(offset,from)有两个参数
offset：偏移量
from：方向
0：表示文件开头
1：表示当前位置
2：表示文件末尾
'''

# demo：把位置设置为：从文件开头偏移5个字节

# 打开一个已经存在的文件
f=open("test.txt","r")
str=f.read(10)
print("读取的数据是：%s" %str)

f.seek(1,0)
# 查找当前位置
position=f.tell()
print("当前的位置是：%s" %position)
f.close()