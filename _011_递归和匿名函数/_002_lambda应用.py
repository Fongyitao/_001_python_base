def test(a,b,func):
    return func(a,b)

print(test(22,33,lambda x,y:x+y))# 55

stus=[{"name":"Ryan","age":23},{"name":"Jack","age":18}]

#匿名函数的作用：返回了列表中字典key为name的值，再有sort对其进行排序
stus.sort(key=lambda x:x["name"],reverse=True) #采用降序排序，默认reverse=False是升序排序

print(stus)