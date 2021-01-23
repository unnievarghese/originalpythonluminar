//lambda in javascript is arrow function ==>
//map()
//filter()
//reduce()
//sort()

// add=(num1,num2)=>{
//     let res=num1+num2
//     console.log(res)
// }
// cube=num=>num**3
// sub=(num1,num2)=>(num1-num2)
// arr=[6,5,4,2,11,12]
// arr.sort((num1,num2)=>num1-num2)
// console.log(arr)
// var arr=[6,5,4,2,11,12]
// var sq=arr.map(num=>num**2)
// console.log(sq)
var arr=[6,5,4,2,11,5,12]
//var sq=arr.map(num=>num**2)
//arr.map(num=>num**2).forEach(sq=>console.log(sq))
console.log(Array.from(new Set(arr)).sort((n1,n2)=>n1-n2))