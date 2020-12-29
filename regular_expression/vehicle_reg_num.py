from re import *
reg_num=input()
pattern='KL[\d]{2}[A-Z]{1,2}[\d]{1,4}'
if fullmatch(pattern,reg_num):
    print('valid reg_num')
else:
    print('invalid reg_num')