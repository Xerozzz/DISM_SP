class Rectangle{
    constructor(length,width){
        this.width=width
        this.length=length
    }

    getArea(){
        return this.width * this.length
    }

    getPerimeter(){
        return this.width*2 + this.length*2
    }
}

var r1 = new Rectangle()
r1.length = 10
r1.width = 5
console.log("Area of rectangle r1 is " + r1.getArea() + "\nPerimeter of rectangle r1 is " + r1.getPerimeter())