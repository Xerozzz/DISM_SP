var input=require("readline-sync")
var number=input.question("Enter any number or (0) to quit: ")

while(number!=0){
    if (number%3==0 ||number%5!=0){
        console.log("12 is divisible by 3 but not 5? true")
    }
    else{
        console.log("12 is divisible by 3 but not 5? false")
    }
    number=input.question("Enter any number or (0) to quit: ")
}
console.log("Program Terminated...")