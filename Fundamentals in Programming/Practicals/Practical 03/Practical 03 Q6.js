var input=require("readline-sync");
var firstInteger = parseInt(input.question("Enter first number:"))
var secondInteger=parseInt(input.question("Enter second number:"))
var divisible
var total=firstInteger+secondInteger
if (firstInteger%secondInteger==0){
    divisible= true;
}
else{
    divisible=false;
}
console.log(firstInteger + " + " + secondInteger + " = " + total)
console.log(firstInteger +" divisible by " +secondInteger + "? " +divisible)