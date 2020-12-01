list=[2,1,3,4,6,7]
list=sorted(list)
low=0
upp=len(list)-1
element= int(input())
while(low<upp):
    total=list[low]+list[upp]
    if(element<total):
        upp=upp-1
    if(element>total):
        low=low-1
    elif(element==total):
        print(list[low],list[upp])
        break