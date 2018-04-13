
luck_nu = 9

while True:
    input_nu = int(input("请输入你猜测的数字:"))
    if input_nu == luck_nu:
        print("bingo!")
        break
    else:
        print("error!,再猜一次")
