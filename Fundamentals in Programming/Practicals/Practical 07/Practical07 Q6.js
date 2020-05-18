var i = 1
var num = ""
var line = ""
while (i < 21) {
    num = (Math.random()*10).toFixed()
    line += num + " "
    if (i%4 ==0){
        line= line + "\n"
    }
    i++
}
console.log(line)