# age=int(input())
# if age<18:
#     raise Exception('invalid age')

num=input()
if type(num)!='int':
    raise Exception('only integers allowed')