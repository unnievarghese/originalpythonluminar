patter='ABABAC'
dict={}
for letter in patter:
    if letter not in dict:
        dict[letter]=1
    else:
        print(letter)
        break