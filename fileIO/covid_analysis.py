listofvalue1=[]
dict={}
file=open('covid_19.csv')
for lines in file:
    words=lines.rstrip('\n').lstrip('\ufeff').split(',')
    words[3]=words[3].rstrip('***')
    if words[3] not in dict:
        dict[words[3]]=words[8]
    else:
        dict[words[3]]=words[8]
for key in dict:
    dict[key]=int(dict[key])
high=max(dict,key=dict.get)
low=min(dict,key=dict.get)
print('state with high confirmed cases:',high+'\n'+'state with lw confirmed cases:',low)
list_values=list(dict.values())
list_values=sorted(list_values,reverse=True)
for cases in list_values:
    for key in dict:
        if dict[key]==cases:
            print(key)