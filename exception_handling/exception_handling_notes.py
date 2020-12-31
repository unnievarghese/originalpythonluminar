no1=int(input('enter the no1'))
no2=int(input('enter the no2'))
try:
    res=no1/no2
    print(res)
except Exception as e:
    print(e.args[0])
print('code ran success')