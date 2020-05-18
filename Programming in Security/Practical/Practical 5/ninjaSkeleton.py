# Practical 5, Optional Qn. Class and inheritance
# skeleton file: 
# one of the possible solutions
from turtle import Turtle
from turtle import Screen
import random
class Ninja(Turtle): #note that this extends the class
    ended = False
    def __init__(self):
        
        
        # Your task : need to invoke the parent class's constructor
        

        # make sure self is up, shape is a turtle. color is red
        self.up()
        self.color("red") #change this later to read from a list using a random number
        self.shape("turtle")

        # Your task: set the inital position of the Ninja at (x,y)
        # where x can be any value between (-150..150)
        # and y can be any value between (-150..150)

      

        # Your task: make this ninja to head for a random direction.
        
        
    def walk(self):
        # your task : add in your code to ...
        #   randomly turn from -45 to 45 degree to the left.
   
        # Your task : move this turtle go forward for 5 to 25 steps
 
    
        # if hit / go beyond the border then
        #   hide this turtle image
        #   set self.ended to True
        curX, curY = self.pos()
        if curX <= -400 or curX >= 400 or curY <= -300 or curY >= 300:
            self.hideturtle()
            self.ended = True
            
# main program
# Get hold of a singleton Screen Object (all Turtle Ninja will display on it)
win=Screen()
# set the win width and height to some reason values.
win.setup(800,600)

ninjaList = []
# Your task : create 20 instances of Ninja, append them all into the ninjaList []

 
#####
while len(ninjaList)>0: # loop until no more active Ninja
    # Your task:
    # extract the first ninja object from the ninjaList
    # ie. ninjaList will get 1 object less after this extraction.
    # invoke the walk method on the extracted ninja.
    
    # Your task:
    # if the extracted ninja is ended , destroy it
    # else append it back to the ninjaList
     
    #
    # end of while loop. No more ninja object left.
win.clear()
#win.bye() #quit from the window mode
win.exitonclick() # user click on the window will terminate the program.

