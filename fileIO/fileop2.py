#print unique numbers from data.txt
f=open('data','r')
lst=[]
for con in f:
    con=con.rstrip('\n')
    if con not in lst:
        lst.append(con)
print(lst)

# or can be easily done using a set instead of list
f=open('data','r')
st=set()
for con in f:
    st.add(con.rstrip('\n'))
print(st)
