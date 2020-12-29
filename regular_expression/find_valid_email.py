from re import *
f_in=open('email_list')
email_set=set([i.rstrip('\n') for i in f_in])
pattern="[a-z0-9_-]+@[a-z]+\.[a-z]+"
f_out=open("valid_email_list",'w')
for i in email_set:
    if fullmatch(pattern,i):
        f_out.write(i+'\n')