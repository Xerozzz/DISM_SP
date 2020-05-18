var input= require('readline-sync')
var firstNumber=parseInt(input.question("Please enter the first number."))
var secondNumber=parseInt(input.question("Please enter the second number."))
if (firstNumber > secondNumber) {
    console.log("1st number is bigger")
}
else if (secondNumber > firstNumber) {
    console.log("2nd number is bigger")
}
else {
    console.log("Both numbers are the same")
}