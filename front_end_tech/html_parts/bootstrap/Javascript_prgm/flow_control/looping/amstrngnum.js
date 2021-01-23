function amstrong(num){
    var power=num.toString().length;
    var sum=0
    while(num!=0){
        var digit=num%10
        sum=sum+(digit**power)
        num=Math.floor(num/10)
    }
    console.log(sum)
}
amstrong(123)