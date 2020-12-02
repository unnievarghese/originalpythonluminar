string='AABtBlB'
lst=list(string)
for letter in lst:
    if letter in lst[lst.index(letter)+1:]:
        print(letter)
        break