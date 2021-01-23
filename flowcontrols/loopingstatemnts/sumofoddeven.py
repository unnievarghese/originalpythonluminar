ll=int(input("enter the lowerlimti"))
ul=int(input("enter the upperlimti"))
odd_sum=even_sum=0
for i in range(ll,ul):
    if(i%2!=0):
        odd_sum+=i
    elif(i%2==0):
        even_sum+=i
print('odd_sum=',odd_sum)
print('even_sum=',even_sum)