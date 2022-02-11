import pandas
import turtle

turtle.color("black")
data=pandas.read_csv("50_states.csv")
data_state=data.state.to_list()

screen=turtle.Screen()
screen.title("u.s.a")
image="1.gif"
screen.addshape(image)
turtle.shape(image)

screen.title("census")
screen.screensize(600,600)
count=0
game=True
while game:
    for i in data_state:
        stored_data=data[data.state==i]
        tim=turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.speed(0)
        tim.goto(int(stored_data.x),int(stored_data.y))
        tim.write(stored_data.state.item())
        count+=1
    if count<=50:
        game=False

screen.exitonclick(
