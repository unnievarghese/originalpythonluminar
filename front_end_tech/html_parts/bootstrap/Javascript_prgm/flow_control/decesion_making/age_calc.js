var birthyear=Number(prompt("enter the year:"))
var birthmonth=Number(prompt("enter the month:"))
var birthday=Number(prompt("enter the day:"))
var currentyear=Number(prompt("enter the year:"))
var currentmonth=Number(prompt("enter the month:"))
var currentday=Number(prompt("enter the day:"))

if (currentmonth>birthmonth){
    age=currentyear-birthyear}
else{
    age=currentyear-birthyear-1}
if (currentmonth===birthmonth){
    if (currentday>=birthday){
        age=currentyear-birthyear}
    else{
        age = currentyear - birthyear-1}}
console.log("age is ",age)