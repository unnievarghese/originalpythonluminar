f=open('covid_19.csv')
dict={}
for lines in f:
    word=lines.rstrip('\n').lstrip('\ufeff').split(',')
    if word[3] not in dict:
        dict[word[3]]={'confirmed':word[8],'death': word[7],'cured': word[6]}
    else:
        dict[word[3]] = {'confirmed': word[8],'death': word[7],'cured': word[6]}
def find(**arg):
    state=arg.get('name_of_state')
    detail=arg.get('detail')
    if state in dict:
        if detail in dict[state]:
            print('The',detail,'cases in',state,'is:',dict[state][detail])
        else:
            print('not found')
    else:
        print('not found')
a=input("enter name of state:")
b=input("enter the detail needed:")
find(name_of_state=a,detail=b)