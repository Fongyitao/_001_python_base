#求1-100之间整数和

sum=0
i=1
while i<=100:
    sum+=i
    i+=1
print("1-100整数和为:%d"%sum)
#求1-100之间偶数和:

sum2 = 0
j = 1
while j <= 100:
    if  j%2 == 0:
        sum2+=j
    j+=1

print(sum2)