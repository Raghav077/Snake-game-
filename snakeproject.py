import turtle
import random

w = 500
h = 500
fs = 10
d = 100

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def reset_game():

    global snake, direction, food_position, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    direction = "up"
    food_position = generate_food()
    food.goto(food_position)
    update_snake()

def update_snake():
    global direction

    # Calculate new head position
    new_head = snake[-1].copy()
    new_head[0] += offsets[direction][0]
    new_head[1] += offsets[direction][1]

    if new_head in snake[:-1]:
        reset_game()
    else:
        snake.append(new_head)

        if not food_eaten():
            snake.pop(0)

        if snake[-1][0] > w / 2:
            snake[-1][0] -= w
        elif snake[-1][0] < -w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h

        pen.clearstamps()
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        screen.update()
        turtle.ontimer(update_snake, d)

def food_eaten():

    global food_position
    if distance(snake[-1], food_position) < 20:
        food_position = generate_food()
        food.goto(food_position)
        return True
    return False

def generate_food():

    x = random.randint(-w // 2 + fs, w // 2 - fs) // 20 * 20
    y = random.randint(-h // 2 + fs, h // 2 - fs) // 20 * 20
    return (x, y)

def distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake Game")
screen.bgcolor("green")
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("white")
food.shapesize(fs / 20)
food.penup()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")

reset_game()
turtle.done()
