//Check why the enlarge and shrinking is not working

class Circle {
    constructor(radius){
        this.radius=radius
    }

    getArea(){
        return Math.PI * (this.radius **2)
    }
    
    enlargeCircle(){
        return this.radius*3
    }

    shrinkCircle(){
        return this.radius/2
    }
}

var circle1 = new Circle(2)
console.log("Area of circle1 with radius " + circle1.radius + " is " + circle1.getArea())
circle1.radius=circle1.enlargeCircle()
console.log("Circle is enlarged 3 times.\nArea of circle1 with radius " + circle1.radius + " is " + circle1.getArea())
circle1.radius=circle1.shrinkCircle()
console.log("Circle is shrunk by halve.\nArea of circle1 with radius " + circle1.radius + " is " + circle1.getArea())