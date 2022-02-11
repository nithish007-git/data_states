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
gussed_state=[]
while len(gussed_state)<50:
        answer = screen.textinput(title=f"{len(gussed_state)}/50", prompt="enter").title()
        if answer=="Exit":
            miss=[]
            for i in data_state:
                if i not in gussed_state:
                    miss.append(i)
            data_final = pandas.DataFrame(miss)
            data_final.to_csv("final.csv")
            break
        if answer in data_state:
            gussed_state.append(answer)
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()

            data1 = data[data.state == answer]
            tim.goto(int(data1.x), int(data1.y))
            tim.write(data1.state.item())





screen.exitonclick()