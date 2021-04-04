import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0
height = 500
width = 500
pixels = 20
snake_body = []


#This is to open a file so the scores can be saved
scorelist = open("highscore.txt","w")
scorelist.close


#The window the game is played in
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width = width, height = height)
#Turns of screen updates to allow it to go faster
window.tracer(0)

#The head of the snake
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("green")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = "stop"

#The food the snake eats
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
#Randomly selects a starting point for the apple within the screen
apple.goto(random.randint(((width/-2)+10),((width/2)-10)),random.randint(((height/-2)+10),((height/2)-10)))

#Makes the score at the top
words = turtle.Turtle()
words.speed(0)
words.shape("square")
words.color("white")
words.penup()
words.hideturtle()
words.goto(0, ((height/2) - 50))
words.write("Score: 0   High Score: 0", align = "center", font = ("Times New Roman", 24, "normal"))

def up():
	if snake_head.direction != "down":
	 snake_head.direction = "up"
	
def down():
	if snake_head.direction != "up":
		snake_head.direction = "down"
                                         
def left():
	if snake_head.direction != "right":
		snake_head.direction = "left"
	
def right():
	if snake_head.direction != "left":
		snake_head.direction = "right"

#The up, down, left, and right functions allow you to move in
#all four directions as long as you do not try to go in the
#opposite direction you are going 

def movement():
	if snake_head.direction == "up":
		# sets the y coordinate to y and moves it up a set amout of pixels
		y = snake_head.ycor()
		snake_head.sety(y + pixels)
		
	if snake_head.direction == "down":
		# sets the y coordinate to y and moves it down a set amout of pixels
		y = snake_head.ycor()
		snake_head.sety(y - pixels)
		
	if snake_head.direction == "left":
		# sets the x coordinate to x and moves it left a set amount of pixels
		x = snake_head.xcor()
		snake_head.setx(x - pixels)
		
	if snake_head.direction == "right":
		# sets the x coordinate to x and moves it right a set amount of pixels
		x = snake_head.xcor()
		snake_head.setx(x + pixels)

	#Allows you to move snake with arrow keys
def arrow_keys():
	window.listen()
	window.onkeypress(up, "Up")
	window.onkeypress(down, "Down")
	window.onkeypress(left, "Left")
	window.onkeypress(right, "Right")
	
	#Allows you to move snake with WASD
def wasd():
	window.listen()
	window.onkeypress(up, "w")
	window.onkeypress(down, "s")
	window.onkeypress(left, "a")
	window.onkeypress(right, "d")
	
def get_score():
  #adds 10 points to the score and sets the high_score

	global score
	global high_score
	
	score += 10
		
	if score > high_score:
		high_score = score
		
		
	words.clear()
	words.write("Score: {}   High Score: {}".format(score, high_score), align = "center", font = ("Times New Roman", 24, "normal"))


	#Moves apple when snake eats it and adds length to snake
def eat_apple():

		#Makes the snake hit the apple
	if snake_head.distance(apple) < pixels:
		x = random.randint(((width/-2)+10),((width/2)-10))
		y = random.randint(((height/-2)+10),((height/2)-10))
		apple.goto(x, y)
		
		new_snake_body = turtle.Turtle()
		new_snake_body.speed(0)
		new_snake_body.shape("square")
		new_snake_body.color("light green")
		new_snake_body.penup()
		snake_body.append(new_snake_body)
		#This adds to the body when snake eats apple
		
		global delay
		
		delay -= .001
		
		get_score()
		
	# moves the body together
	move_body()
	
	
def move_body():
	for sq in range(len(snake_body) -1, 0, -1):
		#Moves the x and y coordinates to the next space
		#keeps the body moving together
		#does not include the first body part
		x = snake_body[sq - 1].xcor()
		y = snake_body[sq - 1].ycor()
		snake_body[sq].goto(x,y)
		
	if len(snake_body) > 0:
		#moves the first body part with the head
		x = snake_head.xcor()
		y = snake_head.ycor()
		snake_body[0].goto(x,y)
		

def parameters():
	#Makes it so if you hit the border you lose
	if snake_head.xcor() > ((width/2) - 10) or snake_head.xcor() < ((width/-2) + 10) or snake_head.ycor() > ((height/2) - 10) or snake_head.ycor() < ((height/-2) + 10):
		time.sleep(1)
		snake_head.goto(0,0)
		snake_head.direction = "stop"
		
		#Sets snake to default position and resets score
		reset()
			
		
def body_hit():
	#If you hit yourself you lose
	for sq in snake_body:
		if sq.distance(snake_head) < pixels:
			time.sleep(1)
			snake_head.goto(0,0)
			snake_head.direction = "stop"

			#Sets snake to default position and resets score
			reset()
	

def reset():

	global score
	global delay
			
	score = 0
	delay = 0.1
			
	words.clear()
	words.write("Score: {}   High Score: {}".format(score, high_score), align = "center", font = ("Times New Roman", 24, "normal"))
	#Sets score back to zero
	
	for sq in snake_body:
		#gets rid of the previous body
			sq.hideturtle()
			
		#resets the list that hold the body
	snake_body.clear()
	
	#appends the score to the file we created
	saved_score = open("highscore.txt","a")
	saved_score.write(str(input("score: ")))
	saved_score.write("\n")
		
	saved_score.close()
	

		
def main():

	#Allows you to use arrow keys or WASD
	arrow_keys()
	wasd()

	
	while True:
		window.update()
		
		#If you hit the border you lose
		parameters()
		
		#Moves apple when the snake eats it and adds lenght to snake
		eat_apple()
			
		#Moves the snake a set amount of pixels in the direction it is set
		movement()
		
		#If you hit yourself you lose
		body_hit()
		
		#sets the delay of the snakes movements
		time.sleep(delay)

	window.mainloop()

	
if __name__ == "__main__":
	main()