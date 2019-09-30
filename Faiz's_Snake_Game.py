import turtle
import time
import random
import winsound
delay=0.1
segments=[]
score=0
high_score=0
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
                
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_right():
    if head.direction!="left":
        head.direction="right"
def go_left():
    if head.direction!="right":
        head.direction="left"
        
win=turtle.Screen()
win.title("Faiz's snake game")
win.bgcolor("blue")
win.setup(width=1600,height=850)
win.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,100)
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.80,0.80)
food.goto(0,0)

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,370)
pen.write("Score: 0 High Score: 0",align="center",font=("Courier",24,"normal"))
win.listen()
win.onkey(go_up,"w")
win.onkey(go_down,"s")
win.onkey(go_right,"d")
win.onkey(go_left,"a")

while True:
    win.update()    
    if head.xcor()>740 or head.xcor()<-740 or head.ycor()>395 or head.ycor()<-395:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"        
        for i in segments:
            i.goto(1000,1000)
        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),align="center",font=("Courier",24,"normal"))
    if head.distance(food)<20:
        x=random.randint(-740,740)
        y=random.randint(-395,395)
        food.goto(x,y)
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)
        winsound.PlaySound("bounce,wav",winsound.SND_ASYNC)
        delay=delay-0.001
        score=score+10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score), align="center",font=("Courier",24,"normal"))
    for j in range(len(segments)-1,0,-1):
        x=segments[j-1].xcor()
        y=segments[j-1].ycor()
        segments[j].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for k in segments:
                k.goto(1000,1000)
            segments.clear()
            delay=0.1
            score=0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))
    time.sleep(delay)
win.mainloop()
            



