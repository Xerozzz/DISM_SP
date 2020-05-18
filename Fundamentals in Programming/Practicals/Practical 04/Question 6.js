var input=require("readline-sync")
var rate, cost 
var discount=0.7
var type=input.question("Enter bicycle type (number):\n(1) Single Seater     (2)Double Seater")
var hours=parseInt(input.question("Enter number of hours rented:"))

if (type=="1"){                         
    rate=5.50
    cost=rate * hours
    if (hours>=3){
        cost=cost * discount
    }
}
if (type=="2"){
    rate=7.8
    cost=rate*hours
    if (hours>=3){
        cost=cost*discount
    }
}
cost=cost.toFixed(2)
console.log("Total Rental Fee: $"+cost)
