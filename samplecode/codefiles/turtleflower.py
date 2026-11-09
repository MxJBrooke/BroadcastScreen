import turtle
def petal():
  for i in range (0,8):
      turtle.forward(50)
      turtle.right(45)    

turtle.width(3)
turtle.pencolor("blue")
for i in range(0,10): 
    petal()  
    turtle.right(36)
