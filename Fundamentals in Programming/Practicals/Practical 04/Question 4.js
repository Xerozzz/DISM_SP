var input=require('readline-sync')

var years=parseInt(input.question("Please enter your years of service:"))
var salary=parseInt(input.question("Please enter your salary:"))

if (years < 10 && salary < 1000){
    console.log("Your increment is $100")
}
else if (years < 10 && salary < 2000){
    console.log("Your increment is $200")
}
else if (years < 10 && salary > 1999){
    console.log("Your increment is $300")
}
else if (years > 10 && salary < 1000){
    console.log("Your increment is $200")
}
else if (years > 10 && salary < 2000){
    console.log("Your increment is $300")
}
else if (years > 10 && salary > 1999){
    console.log("Your increment is $400")
}