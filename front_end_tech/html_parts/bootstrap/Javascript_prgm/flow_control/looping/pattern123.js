str=''
for (let row=1;row<=5;row++){
    for(let col=1;col<=row;col++){
        str=str+String(row)+' '
    }
    console.log(str)
    str=''
}