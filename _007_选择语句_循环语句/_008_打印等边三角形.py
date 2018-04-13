
'''
* * * *
 * * *
  * *
   *
'''
a=int(input("请输入边长:"))
i=0
while i<a:
    k=0
    while k<i:
        print(end=" ")
        k+=1
    j = 0
    while j<a-i:
        print("*",end=" ")
        j+=1
    i+=1
    print()
