import turtle




screen = turtle.Screen()


screen.setup(800, 800)


screen.bgcolor('pink')
t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle()
t2.showturtle()
t3 = turtle.Turtle()
t3.showturtle()
t3.hideturtle()


t.hideturtle()
t2.hideturtle()


t.speed(2000)
t.penup()
t.goto(-5,-70)
t.pendown()
t.fillcolor("Cornflower Blue")
t.begin_fill()
t.circle(175)
t.end_fill()


t.penup()
t.goto(150,-110)
t.pendown()
t.fillcolor('hot pink')
t.begin_fill()
t.circle(30)
t.end_fill()



t.penup()
t.goto(0,50)
t.pendown()
t.fillcolor('hot pink')
t.begin_fill()
t.circle(30)
t.end_fill()




t.penup()
t.goto(-150,-110)
t.pendown()
t.fillcolor('hot pink')
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(150,250)
t.showturtle()
t.pendown()
t.fillcolor("hot pink")
t.begin_fill()
t.circle(25)
t.left(90)
t.circle(25)
t.left(90)
t.circle(25)
t.left(90)
t.circle(25)
t.end_fill()

t.penup()
t.goto(-150,250)
t.showturtle()
t.pendown()
t.fillcolor("hot pink")
t.begin_fill()
t.circle(25)
t.left(90)
t.circle(25)
t.left(90)
t.circle(25)
t.left(90)
t.circle(25)
t.end_fill()



t.penup()
t.goto(-220,50)
t.pendown()
t.fillcolor('hot pink')
t.begin_fill()
t.setheading(45)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

t.end_fill()

t.penup()
t.goto(220,50)
t.pendown()
t.fillcolor('hot pink')
t.begin_fill()
t.setheading(45)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

t.end_fill()




t2.penup()
t2.goto(0, 100)
t2.pendown()
t3.penup()
t3.goto(0, 200)
t.penup()
t.goto(0, 150)
t.pendown()
t.write("All About Me", font=("Courier", 30, "bold"), align="center")
t.penup()
t.goto(0,-20)
t.pendown()
t.write("Lexi Cilia", font=("Courier", 30, "bold"), align="center")
t.showturtle()
t.clear()


t.penup()
t.goto(0,250)
t.write("My favorite food", font=("arial", 30, "bold"), align="center")


turtle.addshape("tacos.gif.png")
t.shape("tacos.gif.png")
t.goto(150,150)
a = t.stamp()
t.hideturtle()
t.goto(150,200)
t.write("Tacos", font=("arial", 30, "bold"), align="center")


turtle.addshape("strawberry.png")
t.shape("strawberry.png")
t.goto(0,0)
b = t.stamp()
t.goto(0,50)
t.write("Strawberry", font=("arial", 30, "bold"), align="center")
turtle.addshape("pasta.gif")
t.shape("pasta.gif")
t.goto(-150,-150)
c = t.stamp()
t.goto(0,0)
t.goto(-150,-100)
t.write("Pasta", font=("arial", 30, "bold"), align="center")
t.clear()
t.clearstamps()
t.penup()
t.goto(0,200)
t.write("My favorite hobbies", font=("arial", 30, "bold"), align="center")


turtle.addshape("sleep.png")
t.shape("sleep.png")
t.goto(150,150)
a = t.stamp()
t.hideturtle()




turtle.addshape("dance.png")
t.shape("dance.png")
t.goto(0,0)
b = t.stamp()


turtle.addshape("cheer.png")
t.shape("cheer.png")
t.goto(-150,-150)
c = t.stamp()
t.goto(0,0)
t.clear()
t.clearstamps()
t.penup()
t.goto(0,200)
t.write("My favorite movie", font=("arial", 30, "bold"), align="center")


turtle.addshape("movie.png")
t.shape("movie.png")
t.goto(-150,-150)
c = t.stamp()
t.goto(0,0)

t.clear()
t.clearstamps()
t.penup()
t.goto(0,200)
t.write("My favorite sport", font=("arial", 30, "bold"), align="center")

turtle.addshape("hockey.png")
t.shape("hockey.png")
t.goto(-150,-150)
c = t.stamp()
t.goto(0,0)







turtle.done()




