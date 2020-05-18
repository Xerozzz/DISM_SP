

class BankAccount{
    constructor(name,savings){
        this.name = name
        this.savings = parseFloat(savings)
    }

    getBalance(){
        return this.name + " has $" + this.savings.toFixed(2)
    }
}

var oliver = new BankAccount("Oliver Twist", 1000)
var richie = new BankAccount("Richie Rich",100000)

console.log(oliver.getBalance())
console.log(richie.getBalance())