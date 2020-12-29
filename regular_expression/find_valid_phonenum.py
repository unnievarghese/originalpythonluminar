from re import *
f=open('phone_number_list')
set_phone=[i.replace(' ','').rstrip('\n') for i in f]
pattern=compile(r'(^\+91[7896][\d]{9})|[0]?[7896][\d]{9}')
fout=open('valid_phone_num','w')
for i in set_phone:
    if fullmatch(pattern,i):
        fout.write(i+'\n')