str=''
for (let i=1;i<13;i++){
    str=str+i+'\t'
    if (i%4===0){
        console.log(str)
        str=''
    }
}