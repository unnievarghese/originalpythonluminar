limit=int((input("entert the limit:")))
liste=[]
listo=[]
for n in range(1,limit+1):
    if(n%2==0):
        liste.append(n)
    else:
        listo.append(n)
print(liste)
print(listo)