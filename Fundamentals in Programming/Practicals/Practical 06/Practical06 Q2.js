var input=require("readline-sync")
var a_grade=0
var marks=new Array()
for(var i=0;i<10;i++){
    var student_count=i+1
    marks[i]=input.question("Enter marks for student #" + student_count + ": ")
    if (marks[i] > 79){
        a_grade += 1
    }
}
console.log(a_grade + " students scored A grade.")