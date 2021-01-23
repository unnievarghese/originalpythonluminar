num1=Number(prompt('enter num1'))
num2=Number(prompt('enter num2'))
num3=Number(prompt('enter num3'))
if(num1>num2 && num1>num3){
    if(num2>num3){
        console.log("2nd large is ",num2)}
    else{
        console.log("2nd large is ",num3)}}
else if(num2>num1 && num2>num3){
    if (num1 > num3){
        console.log("2nd large is ",num1)}
    else{
        console.log("2nd large is ",num3)}}
else if(num3>num2 && num3>num1){
    if (num1 > num2){
        console.log("2nd large is ",num1)}
    else{
        console.log("2nd large is ",num2)}}
else if(num1===num2===num3){
    console.log("all num equal")}