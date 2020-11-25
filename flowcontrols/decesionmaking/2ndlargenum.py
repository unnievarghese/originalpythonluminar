num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
if(num1>num2 and num1>num3):
    if(num2>num3):
        print("2nd large is ",num2)
    else:
        print("2nd large is ",num3)
elif(num2>num1 and num2>num3):
    if (num1 > num3):
        print("2nd large is ",num1)
    else:
        print("2nd large is ",num3)
elif(num3>num2 and num3>num1):
    if (num1 > num2):
        print("2nd large is ",num1)
    else:
        print("2nd large is ",num2)
elif(num1==num2==num3):
    print("all num equal")
