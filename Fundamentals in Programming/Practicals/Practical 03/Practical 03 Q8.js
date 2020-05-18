var input=require("readline-sync")
var X1=parseInt(input.question("Enter X1"))
var Y1=parseInt(input.question("Enter Y1"))
var X2=parseInt(input.question("Enter X2"))
var Y2=parseInt(input.question("Enter Y2"))
var firstPoint="("+X1+","+Y1+")"
var secondPoint="("+X2+","+Y2+")"
var xEqn=(X2-X1)**2
var yEqn=(Y2-Y1)**2
var distance=(Math.sqrt(xEqn+yEqn)).toFixed(4)
console.log("The distance between " + firstPoint +" and " + secondPoint +" is " +distance)

