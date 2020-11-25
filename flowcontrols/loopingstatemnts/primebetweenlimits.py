ll = int(input("enter the lower limit:"))
ul = int(input("enter the upper limit:"))
flag = 0
for num in range(ll, ul + 1):
    for i in range(2, num):
        if (num % i == 0):
            flag = 1
            break
    if (flag == 0):
        print(num, end=",")
    flag=0
