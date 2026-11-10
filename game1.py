import random
import turtle as t

trlist = ("tr0", "tr1", "tr2", "tr3", "tr4")
tr = {}
for obj in trlist:
    tr[obj] = t.Turtle()

tscreen = t.Screen()
tu = t.Turtle()
td = t.Turtle()
tf = t.Turtle()
tscreen.bgcolor("black")
#x -300~300
#y -250~250

score = int(0)
reset = True
failcount = int(0)

tf.speed(0)
td.speed(0)
tf.up()
td.up()
tf.ht()
td.ht()
td.goto(200, 250)
tf.goto(200,200)
t.hideturtle()

def updateScore(score_local):
    td.clear()
    td.color("white")
    td.write(f"Score: {score_local}", font = ("Arial", 20 , "bold"))

def updateFailcount(failcount_local):
    tf.clear()
    tf.color("red")
    tf.write(f"Fail = {failcount_local}", font = ("Arial", 20, "bold"))

tu.up()
tu.shape("circle")
tu.color("blue")
tu.shapesize(2, 2)

for obj in trlist:
    tr[obj].up()
    tr[obj].shape("circle")
    tr[obj].color("red")
    tr[obj].shapesize(2, 2)
    tr[obj].speed(0)

tu.speed(0)
tu.goto(0, -250)

def usrLeft():
    tu.setx(tu.xcor() - 15)

def usrRight():
    tu.setx(tu.xcor() + 15)


def main():
    global score
    global reset
    global failcount
    while True:
        if reset == True:
            reset = False
            for obj in trlist:
                tr[obj].goto(random.randrange(-300, 300), 250)
        
        for obj in trlist:
            tr[obj].sety(tr[obj].ycor() - 15)

        for obj in trlist:
            xdist = abs(int(tu.xcor() - tr[obj].xcor()))
            ydist = abs(int(tu.ycor() - tr[obj].ycor()))
            if ydist <= 10:
                if xdist <= 10:
                    score = score + 1
                    updateScore(score)
                    reset = True
                    continue

        for obj in trlist:
            if tr[obj].ycor() < -255:
                reset = True
                failcount = failcount + 1
                updateFailcount(int(failcount / 5))
                continue


tscreen.onkey(usrLeft, "a")
tscreen.onkey(usrRight, "d")
tscreen.onkey(usrLeft, "A")
tscreen.onkey(usrRight, "D")
tscreen.onkey(usrLeft, "Left")
tscreen.onkey(usrRight, "Right")
tscreen.listen()
main()
