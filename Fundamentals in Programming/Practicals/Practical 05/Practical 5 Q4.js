var input=require('readline-sync')
var number=input.question("Enter a number:")
while (number<100 || number>200){
    number=input.question("Error! Please enter a number between 100 and 200.")
}
console.log("Input Accepted: End of program!")