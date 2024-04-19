# --------------------- Library section -----------------------
import random
import turtle as t


# ------------------------ Screen section ---------------------------
screen = t.Screen()
screen.setup(600,600)
screen.title('Snake game')
screen.bgcolor('cyan')
# ------------------------------head section -----------------------
head = t.Turtle()
head.shape('square')
head.color('red')
head.direction = 'right'
head.penup()
head.speed('fastest')
# -------------------------Food -----------------------------
food = t.Turtle()
food.shape('circle')
food.color('green')
food.penup()
x = random.randint(-290,290)
y = random.randint(-290,290)
food.goto(x,y)
food.speed('fastest')
# -----------------------------------------------------------
def up(): head.direction ='up'
def down(): head.direction='down'
def left(): head.direction ='left'
def right(): head.direction ='right'

screen.listen() # listen to any event
screen.onkeypress(up, 'w')
screen.onkeypress(up, 'Up')
screen.onkeypress(down, 's')
screen.onkeypress(down, 'Down')
screen.onkeypress(left, 'a')
screen.onkeypress(left, 'Left')
screen.onkeypress(right,'d')
screen.onkeypress(right,'Right')

def move():
    if head.direction == 'right':
        x = head.xcor() # give you current x cordinate
        head.setx(x + 10)
    elif head.direction == 'left':
        x = head.xcor() # give you current x cordinate
        head.setx(x - 10)
    elif head.direction == 'up':
        y = head.ycor()
        head.sety(y + 10)
    else:
        y = head.ycor()
        head.sety(y - 10)

# --------------- game engine
import time
while True:
    time.sleep(0.1)
    move()
    # --------------------- food detection
    if head.distance(food) < 20 :
        food.goto(random.randint(-290, 290), random.randint(-290,290))

    # ------------------------- wall detection ------------
    if head.xcor() > 290 or head.xcor() < -290:
        head.setx(head.xcor() * -1)

    if head.ycor() > 290 or head.ycor() < -290:
        head.sety(head.ycor() * -1)

    #
 



