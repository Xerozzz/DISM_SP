var input = require("readline-sync")
var rank = getInput()
var money = 0
printPrize(rank)

function getInput(){
    rank=parseInt(input.question("Please enter your rank: "))
    return rank
}

function printPrize(n){
    switch (n){
        case 1 :
            money = 1000
            break;
        case 2 :
            money = 800
            break;
        case 3 :
            money = 700
            break;
        case 4 :
            money = 300
            break;
        case 5 :
            money = 300
            break;
        default:
            money = 20
    }
    console.log("Your prize money is $" + money)
}

