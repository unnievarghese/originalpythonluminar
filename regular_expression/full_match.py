#start with a-k,second chara shud be digit and must be divisilbe by 3,folowed by anu number of char

import re
pattern='[a-kA-k][369][a-zA-Z0-9]*'
variablename=input()
if re.fullmatch(pattern,variablename):
    print('valid')
else:
    print('invalid')
