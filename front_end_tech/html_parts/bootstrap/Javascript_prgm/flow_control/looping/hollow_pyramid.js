str=''
for(let row=1;row<5;row++){
    for (let col=1;col<8;col++){
        if(row===4 || row+col===5 || col-row===3)
            {str=str+'*'+'\t'}
        else 
            { str=str+'\t'}
    }
    console.log(str)
    str=''
}
