var amount,$1000,$100,$50,$10,$5,$2,$1
var input=require("readline-sync")
amount=parseInt(input.question("Enter Amount ($):"))
while (amount>0){
if (amount > 1000){
    $1000=Math.floor(amount/1000);
    amount= amount - (1000* $1000);
}
else if (amount > 100){
    $100=Math.floor(amount/100);
    amount=amount- (100*$100);
}
else if (amount > 50){
    $50=Math.floor(amount/50);
    amount=amount- (50*$50);
}
else if (amount > 10){
    $10=Math.floor(amount/10);
    amount=amount- (10*$10);
}
else if (amount > 5){
    $5=Math.floor(amount/5);
    amount=amount- (5*$5);
}
else if (amount > 2){
    $2=Math.floor(amount/2);
    amount=amount- (2*$2);
}
else if (amount > 1){
    $1=Math.floor(amount/1);
    amount=amount- (1*$1);
}
}
console.log($1000 + " Note(s) of 1000")
console.log($500 + " Note(s) of 500")
console.log($100 + " Note(s) of 100")
console.log($50 + " Note(s) of 50")
console.log($10 + " Note(s) of 10")
console.log($2 + " Note(s) of 2")
console.log($1 + " Note(s) of 1")
