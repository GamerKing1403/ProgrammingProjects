import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
ball = turtle.Turtle()
ball.shape('circle')
ball.goto(0, 200)
ball.goto(100, 200)

ball.color("green")
wn.mainloop()
