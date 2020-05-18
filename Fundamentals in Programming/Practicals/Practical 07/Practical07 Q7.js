var input = require("readline-sync");
var i = 1
var pattern =""
var n = readInput();
var pat = choosePattern();


switch(pat) {
    case "1" :
        printPattern1(n)
        break;
    case "2":
        printPattern2(n)
        break;
    case "3":
        printPattern3(n)
        break;
    default:
        console.log("Exited")
}    

function readInput() { 
    n = input.question("Enter the number of rows: ")
    return n
}

function choosePattern(){ 
    pat=input.question("1. Print Pattern 1\n2. Print Pattern 2\n3. Prine Pattern 3\n4. Exit\n>>")
    return pat
}

function printPattern1(n){ 
    while (i <= n){
        var value= i.toString() + " "
        pattern += value.repeat(n) + "\n"
        i++
    }
    console.log(pattern)
}
function printPattern2(n){ 
    while (i <= n){
        var count=1
        while (count <= n){
            pattern += count + " "
            count++
        }
        pattern += "\n"
        i++
    }
    console.log(pattern)
}

function printPattern3(n){ 
    while (i <=n){
        var value=i
        var count=0
        while (count<n){
            pattern += value + " "
            value += i
            count++
        }
        pattern += "\n"
        i++
    }
    console.log(pattern)
    

}
