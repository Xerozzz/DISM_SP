var input=require('readline-sync')

var score=parseInt(input.question("Please enter your score."))
if (score>=80){
    console.log("Your grade is A")
}
if (score>=70){
    console.log("Your grade is B")
}
if (score>=60){
    console.log("Your grade is C")
}
if (score>=50){
    console.log("Your grade is D")
}
else{
    console.log("Your grade is F")
}