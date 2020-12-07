f=open('employee_data')
dict={}
for line in f:
    word=line.rstrip('\n').split(',')
    if word[0] not in dict:
        dict[word[0]]={'id':word[0],'name':word[1],'designation':word[2],'sallary':word[3]}
def func(**arg):
    id=arg['id']
    detail=arg['detail']
    if id in dict:
        if detail in dict[id]:
            print('The',detail,'of the employee',id,'is:',dict[id][detail])
        else:
            print('not found')
    else:
        print('not found')
a=input()
b=input()
func(id=a,detail=b)