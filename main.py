from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

end = False
while not end:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snakes[0].distance(food) < 10:
        food.create_food()
        snake.increase_size()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.check_high_score()
        score.game_over()
        end = True

    # Detect collision with tail
    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 10:
            score.check_high_score()
            score.game_over()
            end = True









screen.exitonclick()
