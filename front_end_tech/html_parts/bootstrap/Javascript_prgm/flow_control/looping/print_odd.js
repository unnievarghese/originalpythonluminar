function odd(ul,ll){
    arr=[]
    for (let i=ul;i<=ll;i++){
        if(i%2!=0){
            arr.push(i)
        }
    }
    console.log(arr)
}
odd(1,10)