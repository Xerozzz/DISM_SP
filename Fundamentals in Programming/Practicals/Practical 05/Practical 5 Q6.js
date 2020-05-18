var output,value
var input=require("readline-sync")
var num1=parseInt(input.question("Enter 1st number:"))
var num2=parseInt(input.question("Enter 2nd number:"))
output=("Odd numbers between " + num1 +" & " + num2 + ": \n" )
for(num1;num1<num2;num1++){
    if(num1%2==1)
    output= (output + num1 + " ")
}
console.log(output)