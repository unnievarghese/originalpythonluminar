function reverse(num){
    res=0
    while(num!=0){
        digit=num%10
        res=res*10+digit
        num=Math.floor(num/10)}
    console.log(res)}
reverse(123)