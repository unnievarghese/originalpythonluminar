function evenodd(ll,ul){
    odd_sum=even_sum=0
    for (let i=ll;i<ul;i++){
        if(i%2!=0){
            odd_sum+=i}
        else if(i%2===0){
            even_sum+=i}}
    console.log('odd_sum=',odd_sum)
    console.log('even_sum=',even_sum)
}
evenodd(1,10)