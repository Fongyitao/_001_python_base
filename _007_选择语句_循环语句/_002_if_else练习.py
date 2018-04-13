#BMI公式:
'''
体质指数（BMI）=体重（kg）÷身高^2（m）
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
'''

height = float(input("请输入身高(m):"))
weight = float(input("请输入体重(kg):"))

print("身高%.2fm,体重%.2fkg"%(height,weight))
bmi = weight / (height ** 2)
print("BMI指数为:%f"%bmi)
if bmi < 18.5:
    print("过轻")
elif bmi >= 18.5 and bmi <= 23.9:
    print("正常")
elif bmi >= 24 and bmi <= 27:
    print("过重")
elif bmi >= 28 and bmi <= 32:
    print("肥胖")
elif bmi > 32:
    print("非常肥胖")