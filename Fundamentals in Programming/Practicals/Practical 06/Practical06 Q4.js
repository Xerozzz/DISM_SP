intArray= new Array(5)
for(var i=0; i<5;i++){
    intArray[i]=(Math.floor(Math.random()*12))
}
console.log("Elements generated : " + intArray)
var largest=0
for(var i=0;i<intArray.length;i++){
    if (intArray[i] > largest){
        largest = intArray[i]
        console.log(largest + " is swapped.")
    }
}
console.log("Elements of int array : " + intArray +"\nHighest Value : " + largest)