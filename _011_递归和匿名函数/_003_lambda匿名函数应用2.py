def test(a,b,func):
    return func(a,b)

func=input("请输入lambda表达式（例如lambda x,y:x+y）>>")
func=eval(func)# 把字符串转换成表达式

print(test(22,33,func))