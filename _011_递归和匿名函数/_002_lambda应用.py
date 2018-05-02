def test(a,b,func):
    return func(a,b)

print(test(22,33,lambda x,y:x+y))# 55

#----------------------------------

stus=[{"name":"Jack","age":23},{"name":"Ryan","age":18},{"name":"Alice","age":25},{"name":"David","age":35}]

#匿名函数的作用：返回了列表中字典key是name的值，再用sort对值进行排序
stus.sort(key=lambda x:x["name"],reverse=True) #采用降序排序，默认reverse=False是升序排序

print(stus)