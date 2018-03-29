#naomi
#Syuta Sugawara


import  turtle

fin=turtle.Turtle()
fin.pensize(5)

def writeCircle(color):

    fin.color(color)
    fin.pendown()
    fin.circle(50)
    fin.penup()

def lowerRightDiagonal():

    fin.rt(90)

    fin.fd(50)

    fin.lt(90)

    fin.fd(55)


def upperRightDiagonal():

    fin.fd(55)

    fin.lt(90)

    fin.fd(50)

    fin.rt(90)
    

def olympicRing():
    writeCircle("blue")

    lowerRightDiagonal()
    
    writeCircle("yellow")

    upperRightDiagonal()
    
    writeCircle("black")

    lowerRightDiagonal()
   
    writeCircle("green")

    upperRightDiagonal()

    writeCircle("red")


    

fin.ht()
fin.penup()
fin.fd(-110)

olympicRing()
