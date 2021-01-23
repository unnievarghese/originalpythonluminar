var text='hello hai hello how'
var word=text.split(' ')
var count={}
for(i of word){
    if(i in count){
        count[i]+=1
    }
    else{
        count[i]=1
    }}
console.log(count)