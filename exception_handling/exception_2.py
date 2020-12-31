no1=int(input('enter the no1'))
no2=int(input('enter the no2'))
try:
    res=no1/no2
    print(res)
except:
    no2 = int(input('enter the no2'))
    print(no1/no2)
finally:
    print('code ended')