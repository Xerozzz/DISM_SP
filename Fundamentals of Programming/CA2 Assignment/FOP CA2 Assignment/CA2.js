/* Features Present
- More than 3 categories
- Open-Ended Questions
- Random Category
- Navigation Function
- Tells if unanswered question
- Lifeline feature
*/

//Classes
//Open Ended Questions
class OE{  
    constructor(text,correctAnswer){
        this.text=text
        this.correctAnswer=correctAnswer
    }

    //Display Questions
    displayQuestion(q){
        var wholeQuestion = (`Question ${q + 1} : ${this.text}`)
        return wholeQuestion
    }
}
//MCQ Questions
class MCQ{
    constructor(text,options,correctAnswer){
        this.text = text                    //Question
        this.options = options              //Options available stored in an array
        this.correctAnswer = correctAnswer  //Correct answer
    }
    //Displays Questions
    displayQuestion(q){
        var wholeQuestion = (`Question ${q + 1} : ${this.text}`)
        for (var i in this.options){
            var optionNumber = parseInt(i) + 1
            wholeQuestion += (`\n(${optionNumber}) ${this.options[i]}`)
        }
        return wholeQuestion
    }
}
//Actual Quiz
class Quiz{
    constructor(category,typeOfQuestions){
        //Selected category the user decided to try
        this.category = category
        this.typeOfQuestions = typeOfQuestions
        //Making and storing all questions from all categories
        this.allMCQQuestions = [ 
            //IT Questions (MCQ)
            new MCQ(`What is RAM?`, [`Random Access Memory`,`Read Access Memory`,`Read And Make`, `Rapid Accessory Movement`],0),
            new MCQ(`What is ROM?` , [`Registry of Marriage`,`Read Only Memory`,`Random Only Memory`,`Really Old Memory`],1),
            new MCQ(`What is NOT a programming language?` , [`Java`, `C Flat`, `C sharp`, `Python`],1),
            new MCQ(`Which is not a JavaScript Framework?`, [`Python Script`, `JQuery`,`Django`, `NodeJS`],2),
            new MCQ(`Which is used for Connect To Database?`, [`PHP`, `HTML`, `JS`, `All`], 0),
            //Biology Questions (MCQ)
            new MCQ(`The substrate of photo-respiration is ______` , [`Pyruvic acid` , `Glucose` , `Fructose` , `Glycolate`],0),
            new MCQ(`Which one of the following is the infective stage of the Malarial Parasite?`,[`Trophozoite`,`Sporozoite` , `Schigozoite` , `Sporoblast`],1),
            new MCQ(`Which one of these animals is jawless?`, [`Shark`,`Myxine`,`Trygon`,`Sphyrna`],1),
            new MCQ(`Alfa-toxins are produced by _______`, [`Bacteria`,`Fungi`,`Viruses`,`Algae`],1),
            new MCQ(`Allantois of Embryo helps in ______`,[`Excretion`,`Digestion`,`Respiration`,`Protection`],0),
            //Music Questions (MCQ)
            new MCQ(`Which one of the instruments listed belong to the brass family?`,[`Clarinet`,`Trumpet`,`Flute`,`Drums`],1),
            new MCQ(`Which one of these instruments belong to the woodwind family?` , [`Timpani` , `Trombone`, `Flute`,`Tuba`],2),
            new MCQ(`Which one of these instruments is played by moving a long slide?`,[`Trombone`,`Tuba`,`Clarinet`,`Drumset`],0),
            new MCQ(`Which one of these names belong to a famous composer?`,[`Leonard Bernstein`, `Joseph Hayden`, `Jeffrey Aidan`,`Bessie Cow`],0),
            new MCQ(`Which one of these is not commonly found in orchestras?`,[`Violin`,`Oboe`,`Euphonium`,`Timpani`],2),
            //Math Questions (MCQ)
            new MCQ(`What is 5 x 9?`,[`4`,`19`,`45`,`32`],2),
            new MCQ(`Which figure does not have even number of sides?`,[`Square`,`Triangle`,`Rectangle`,`Hexagon`],1),
            new MCQ(`What is 64/8?`,[`8`,`2`,`32`,`16`],0),
            new MCQ(`What is 98-23?`,[`53`,`98`,`75`,`2`],2),
            new MCQ(`What is the square root of 64?`,[`8`,`2`,`4`,`98`],0),
        ]
        this.allOEQuestions=[
            //Math Questions (OE)
            new OE(`What is 6x45?`,`270`),
            new OE(`What is a six sided polygon called?`,`hexagon`),
            new OE(`What is the root of 16?`,`4`),
            new OE(`What is the root of 81?`,`9`),
            new OE(`What is a 8 sided polygon called?`,`octagon`),
            //Song Name Questions (OE)
            new OE(`No tears left to _____`,`cry`),
            new OE(`___ a heartbeat`,`in`),
            new OE(`Every _____ you take`,`breath`),
            new OE(`One _____ time`,`last`),
            new OE(`____ lane`,`penny`),
        ]
        //Selecting Category and Questions that will be asked
        this.selectedQuestions=[]  //To store the questions asked
        //If selected MCQ questions
        if (typeOfQuestions == 1){
            switch(this.category){
                case "IT" :
                    this.selectedQuestions = this.allMCQQuestions.slice(0,5)
                    break;
                case "Biology" :
                    this.selectedQuestions = this.allMCQQuestions.slice(5,10)
                    break;
                case "Music" :
                    this.selectedQuestions = this.allMCQQuestions.slice(10,15)
                    break;
                case "Mathematics" :
                    this.selectedQuestions = this.allMCQQuestions.slice(15,20)
                    break;
                case "Ran" :
                    var count = 19
                    for (var i=0;i < 5;i++){
                        var max = count + 1 
                        var randomNumber = Math.floor(Math.random()*max)
                        this.selectedQuestions.push(this.allMCQQuestions[randomNumber])
                        this.allMCQQuestions.splice(randomNumber,1)
                        count--
                    }
            }
        }
        //If selected open-ended questions
        else if (typeOfQuestions == 2){
            switch(category){
                case "Math":
                    this.selectedQuestions = this.allOEQuestions.slice(0,5)
                    break;
                case "Song":
                    this.selectedQuestions = this.allOEQuestions.slice(5,10)
                    break;
            }
        }
    }

    //Tally marks
    getMarks(){ 
        var marks =0
        if (this.typeOfQuestions==1){
            for(var i in this.selectedQuestions){
                if (this.selectedQuestions[i].correctAnswer == selectedAnswers[i]-1){
                    marks++
                }
            }
        }
        else if (this.typeOfQuestions == 2){
            for(var i in this.selectedQuestions){
                if (this.selectedQuestions[i].correctAnswer == selectedAnswers[i]){
                    marks++
                }
            }
        }
        return marks
    }
    //Check if all questions are answered
    checkIfAnswered(){
        if (this.typeOfQuestions == 1){
            for (var i in selectedAnswers){
                var count = parseInt(i) + 1
                if (quiz.selectedQuestions[i].options[selectedAnswers[i]] == undefined) {
                    console.log(`Question ${count} is not answered/answered properly!`)
                } 
                else {
                    continue
                }
            }
        }
        else if (this.typeOfQuestions == 2){
            for (var i in selectedAnswers){
                var count = parseInt(i) + 1
                if (selectedAnswers[i] == undefined && typeof selectedAnswers[i] != String){
                    console.log(`Question ${count} is not answered properly!`)
                }
                else {
                    continue
                }
            }
        }
    }

    //Output Summary
    outputSummary(){
        if (this.typeOfQuestions == 1){
            for (var i in this.selectedQuestions){
                var count = parseInt(i) + 1
                console.log(`Question ${count}: ${this.selectedQuestions[i].text}\nAnswer: (${selectedAnswers[i]}) ${quiz.selectedQuestions[i].options[selectedAnswers[i]-1]}\n`)
            }
        }
        else if (this.typeOfQuestions == 2){
            for (var i in this.selectedQuestions){
                var count = parseInt(i) + 1
                console.log(`Question ${count}: ${this.selectedQuestions[i].text}\nAnswer: ${selectedAnswers[i]}\n`)
            }
        }
    }
}

//Main Code
var input = require("readline-sync")
var option

//Array for storing user answers
var selectedAnswers = new Array(5)

//Starting of the Quiz to select category and input name
console.log("--=Welcome to the Quiz!=--")
var name = input.question("Please enter your name: ")
typeOfQuestions = input.question(`Hi ${name}, welcome to the quiz! Each quiz will have 5 questions for you to answer. Please choose what types of questions you would like to answer.\n(1) MCQ\n(2) Open-Ended\n>> `)
while (typeOfQuestions != "1" && typeOfQuestions != 2){
    console.log(`Please enter an option above!`)
    typeOfQuestions=input.question(`Hi ${name}, welcome to the quiz! Each quiz will have 5 questions for you to answer. Please choose what types of questions you would like to answer.\n(1) MCQ\n(2) Open-Ended\n>> `)
}
if (typeOfQuestions == 1){
    console.log(`For the MCQ Categories, you can type "5" to get a hint for whichever question you are doing. You can only use this once!\nHowever, if you submit your quiz the first time, this hint is revoked!`)
    option = input.question(`Please choose the category of quiz you would like to attempt: \n(1) IT\n(2) Biology\n(3) Music\n(4) Mathematics\n(5) Random\n>>`)
    while (option !=  "1" && option != "2" && option != "3" && option != "4" && option != "5"){
        console.log("Error! Input must be one of the options above. (1-5)")
        option = input.question("(1) IT\n(2) Biology\n(3) Music\n(4) Mathematics\n(5) Random\n>> ")
    }
    switch (option){
        case "1" :
            console.log("[IT] Category Selected.")
            category = "IT"
            break;
        case "2" :
            console.log("[Biology] Category Selected.")
            category = "Biology"
            break;
        case "3" :
            console.log("[Music] Category Selected.")
            category = "Music"
            break;
        case "4" :
            console.log("[Mathematics] Category Selected")
            category = "Mathematics"
            break;
        case "5" :
            console.log("[Random] Category Selected")
            category = "Ran"
            break;
    }
}
else if (typeOfQuestions == 2){
    option = input.question(`Please choose the category of the quiz you would like to attempt:\n(1) Math\n(2) Song Names\n>>`)
    while (option != 1 & option != 2){
        console.log("Error! Answer must be one of the options above!")
        option = input.question(`Please choose the category of the quiz you would like to attempt:\n(1) Math\n(2) Song Names\n>>`)
    }
    switch(option){
        case "1":
            category = "Math"
            break;
        case "2":
            category = "Song"
            break;
    }
}

//Initiating Quiz
var quiz = new Quiz(category,typeOfQuestions)
var questionNumber = 0
var decision
var lifeline = 1

//Running through the Quiz and questions
while (questionNumber != "x"){
    console.log(quiz.selectedQuestions[questionNumber].displayQuestion(questionNumber))
    if (typeOfQuestions == 2){
        selectedAnswers[questionNumber] = ((input.question(">> ")).toString()).toLowerCase()
    }
    else if (typeOfQuestions == 1){
        selectedAnswers[questionNumber] = (input.question(">> "))
        while (0 > selectedAnswers[questionNumber] || selectedAnswers[questionNumber] > 5){
            selectedAnswers[questionNumber] = parseInt(input.question("Enter an option between 1 and 5!\n>>  "))
        }
        if (selectedAnswers[questionNumber] == 5){
            if (lifeline == 1){
                console.log(`Here is your hint for the answer! The first five characters of the answer is:\n${(quiz.selectedQuestions[questionNumber].options[quiz.selectedQuestions[questionNumber].correctAnswer]).slice(0,5)}`)
                console.log(quiz.selectedQuestions[questionNumber].displayQuestion(questionNumber))
                selectedAnswers[questionNumber] = (input.question(">> "))
                lifeline -= 1
            }
            else {
                console.log("You do not have anymore hints!")
                console.log(quiz.selectedQuestions[questionNumber].displayQuestion(questionNumber))
                selectedAnswers[questionNumber] = (input.question(">> "))
            }
        }
    }
    decision = input.question(`Press \"P\" to go to the previous question, or \"N\" to go to the next question or press \"X\" to submit.\n>> `).toUpperCase()
    while (decision != "X" && decision != "P" && decision != "N"){
        decision = (input.question(`Press \"P\" to go to the previous question, or \"N\" to go to the next question or press \"X\" to submit.\n>> `)).toUpperCase()
    }
    if (decision == "P"){
        if(questionNumber == 0) {
            while (decision != "N" && decision != "X"){
                decision= (input.question(`This is the first question!\n>>`)).toUpperCase()
            }
            if (decision == "N"){
                questionNumber += 1
            }
            else{
                break
            }
        }
        else{
         questionNumber -= 1
        }
    }
    else if (decision == "N"){
        if(questionNumber == 4) {
            while (decision != "P" && decision != "X"){
                decision= (input.question(`This is the last question!\n>> `)).toUpperCase()
            }
            if (decision == "P"){
                questionNumber -= 1
            }
            else{
                break
            }
        }
        else{
         questionNumber += 1
        }
    }
    else if (decision == "X"){
        questionNumber = "x"
    }
}

//Output the quiz summary before submitting
var validation
while (validation != 0){
    quiz.outputSummary()            //Output the summary of the quiz
    quiz.checkIfAnswered()          //Output any unanswered questions
    validation = input.question("Enter 0 to submit your quiz or [1 to 5] to change your answer\n>> ")
    while (validation != "0" && validation !=  "1" && validation != "2" && validation != "3" && validation != "4" && validation != "5"){
        validation = input.question("Enter 0 to submit your quiz or [1 to 5] to change your answer\n>> ")
    }
    if (validation == 0){
        continue
    }
    else if (0 < validation < 6){
        console.log(quiz.selectedQuestions[validation - 1].displayQuestion(validation-1))
        selectedAnswers[validation - 1] = (input.question(">> "))
    }
}

//Finish Submission and Get Marks
var markScored = quiz.getMarks()
var message 
(markScored > 3) ? message = "Well done! You have scored well for the quiz!" : message = "Good effort! Try harder next time!" 
console.log(`Thank you for using this quiz!\nYou have scored ${markScored}/5!\n${message}`)

