import os

"""
OS模块：
1. os.name() -判断现在正在使用的平台，Windows范围'nt' ，Linux返回'posix'
2. os.rename(需要修改的文件名，新的文件名）也可以做剪切
3. os.getcwd()--得到当前工作目录
4. os.listdir() --指定所有目录下所有的文件和目录名。
    以列表的形式全部列举出来，其中没有区分目录和文件
5. os.remove() --删除指定文件
6. os.rmdir() --删除指定目录，该目录不能为空
7. os.mkdir() --创建目录
    想要递归建立目录可以用os.makedirs(x/y/z)
8. os.path.isfile() --判断指定对象是否为文件
9. os.path.isdir() -- 判断是否为目录
10. os.path.exists() --判断指定对象是否存在
11. os.path.split() --返回路径的目录和文件名
12. os.getcwd() --获得当前工作目录
13. os.system() -- 执行shell命令
    例如：os.system("echo 'Hello world'")
14. os.chdir() --改变目录到指定目录
15. os.path.getsize() --获得文件的大小，如果为目录返回0
16. os.path.abspath() -- 获得绝对路径
17. os.path.join(path,name) --连接目录和文件名
18. os.path.basename(path) --返回文件名
19. os.path.dirname(path) --返回文件所在目录
"""

print(os.name) # posix
# os.rename("High Sierra-副本.jpg","High Sierra-copy.jpg")
print(os.path.getsize("High Sierra-copy.jpg")/1024/1024)