import re
#pattern='a+'  #chechk for a and more than 1 occurences of a
#pattern='a*' # a+ like above and zero occurences of a is also checked
#pattern='a?'  # same duty wen pattern='a' plus zero occurences of a is also checked
#pattern='^a'  #starting with a
#pattern='$a'  #starting with a
pattern='a{2,3}'
matcher=re.finditer(pattern,'aaaabaabaca')
for i in matcher:
    print(i.start())
    print(i.group())