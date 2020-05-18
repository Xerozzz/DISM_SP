    var num1=0
var num2=0
var input = require("readline-sync")
num1=getInput("1st")
num2=getInput("2nd")
findMax()

function getInput(s){
    num = input.question("Enter the " + s + " integer: ")
    return num
}

function findMax(){
    if (num1 > num2){
        console.log("1st number is bigger.")
    }
    else if (num2 > num1){
        console.log("2nd number is bigger.")
    }
    else {
        console.log("The 2 numbers are equal.")
    }
}

