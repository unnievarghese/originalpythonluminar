function prime(ll,ul){
    flag=0
    for(let i=ll;i<=ul;i++){
        for(let j=2;j<=Math.floor(i/2);j++){
            if(i%j===0){
                flag=1
            }
        }
    if(flag!=1){console.log(i)}
    flag=0
    }
}
prime(1,20)