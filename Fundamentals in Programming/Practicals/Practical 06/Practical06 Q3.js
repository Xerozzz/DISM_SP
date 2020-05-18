var list1 = [12, 56, 76, 32, 12, 34];
var list2 = [12, 56, 76, 32, 12, 34];
var identical=true
if (list1.length != list2.length){
    console.log("Two lists are not strictly identical")
}
else {
    for(var i=0;i<list1.length;i++){
        if (list1[i]!=list2[i]){
            identical=false
        }
    }
}
if (identical==false){
    console.log("Two lists are not strictly identical.")
}
else{
    console.log("Two lists are strictly identical.")
}