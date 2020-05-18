
class Fan{
    constructor(speed,on){
        this.speed = speed
        this.on = on
    }
    
    getState(){
        if (this.on == 0){
            return "off"
        }
        else{
            switch (this.speed){
                case 1:
                    return "on at slow speed"

                case 2:
                    return "on at medium speed"
                    
                case 3:
                    return "on at fast speed"
                    
            }
        }
    }
}
var fan1 = new Fan(1,1)
var fan2= new Fan(3,1)

console.log("Fan 1 is " + fan1.getState() + "\nFan 2 is " + fan2.getState())
fan1.on = 0
fan2.speed = 2
console.log("\nFan 1 is " + fan1.getState() + "\nFan 2 is " + fan2.getState())
