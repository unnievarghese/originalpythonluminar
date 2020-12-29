from re import *
#pattern='[a-z]'
#pattern='[0-9]'
#pattern='[^0-9]'  #PLEASE NOTE: carret inside the square bracket means except(0-9) in this case.
                  # not starting position, for that ^ is put outside square bracket.
#pattern='[^a-z]' #like mentioned above except a-z
#pattern='[a-zA-Z]'
#pattern='[a-zA-Z0-9]'
#pattern='[^a-zA-Z0-9 ]'
#pattern='\s' #checking for space
#pattern='\S' #checking for anything except space
#pattern='\d' #chechking fo digits
#pattern='\D'#checking for anything except digit
#pattern='\w' #chechking for alphanumeric and _
pattern='\W' #chechking for anything except alphanumeric and _
matcher=finditer(pattern,'abc Z@7k')
for i in matcher:
    print(i.start())
    print(i.group())