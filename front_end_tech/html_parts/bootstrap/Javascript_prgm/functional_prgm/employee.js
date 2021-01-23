var employee=[{id:101,name:'ajay',designation:'qa',sallary:15000},
            {id:102,name:'vijay',designation:'developer',sallary:25000},
            {id:103,name:'sumesh',designation:'coustomer care',sallary:17000},
            {id:104,name:'virat',designation:'developer',sallary:35000},
            {id:105,name:'vinod',designation:'accountant',sallary:20000},
            {id:106,name:'vinodini',designation:"sales",sallary:20000}]

//employee.forEach(emp=>console.log(emp.name))

//covert all name to uppercae
//employee.map(emp=>emp.name).map(nam=>console.log(nam.toUpperCase()))


//print employee according with salary
l=Array.from(new Set(employee.map(emp=>emp.sallary))).sort((num1,num2)=>num1-num2)
for (i of l){
    for (emp of employee){
        if (i == emp.sallary){console.log(emp.name)}
    }
}
