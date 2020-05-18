intArray= new Array(50)
oddArray= new Array()
evenArray= new Array()
for(var i=0; i<50;i++){
    intArray[i]=(Math.floor(Math.random()*101))
    if (intArray[i] % 2 == 0){
        evenArray.push(intArray[i])
    }
    else{
        oddArray.push(intArray[i])
    }
}
console.log("Original Array : \n"+intArray)
console.log("Even Numbers : \n" + evenArray)
console.log("Odd Numbers : \n"+oddArray)