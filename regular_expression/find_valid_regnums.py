import re
f=open('reg_numbs')
fout=open('valid_reg_nums','w')
validregnum=set()
for i in f:
    validregnum.add(i.rstrip('\n'))
pattern='KL[\d]{2}[A-Z]{1,2}[\d]{1,4}'
for i in validregnum:
    if re.fullmatch(pattern,i):
        fout.write(i+'\n')
    else:
        pass