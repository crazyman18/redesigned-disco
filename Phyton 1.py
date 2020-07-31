print("\"Hello, Samuel!\"")

print(3)
print(5 + 3)
print(8 / 2)
print(12 * 6)

name = input("What is your name?")
print(name)

#you can use the format one samuel if you want to place aposthrope
#or the other one.
name = input("What is your name?")
print("Hello  " + name )
print(name + " is a nice name!")
print("\"{} is a nice name!\"".format(name))
print('Python was named after "Monty Python"')
print("And the computer said: \"I'm a computer, silly!\"")

print("Samuel")
print("Monty Python " + "and the Holy Grail")
print("Spam!" * 8)

print("Look, that rabbit's got a vicious streak a mile wide! It's a killer!")
print('We are no longer the knights who say "ni", we are now the knights who say "ekki-ekki-ekki-pitang-zoom-boing!"')
print("There are 10 types of people in this world, those who know \"binary\" and those who don\'t.")

print("""Hitting enter here
does work!""")
print("Here is text \n on two lines")
print("Here is a multi-line \n"
"print statement")

poem = """When you're chewing on life's gristle
Don't grumble, give a whistle
And this'll help things turn out for the best...
And...always look on the bright side of life... 
Always look on the light side of life..."""
print(poem)

phrase = "Today you are feeling: \n"

mood = "Happy"
print(mood)

mood = input("How are you feeling today")
print(mood)
print(phrase + mood)

print(2 * 5 + 3)
#exponent we have BEMDAS operators
print(5 ** 4)
print(18 - 6)

#means first the brackets then next operation
print((7 + 3) / 2)
print(20 - 2 ** 2)
print((5 + 2) * 10)

#integers and floats
result_1 = 8 / 2
result_2 = 3 + 8
result_3 = 0.1 + 0.2
result_4 = 0.1 + 0.7
result_5 = 0.5 + 1
print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)

#Create variables
hourly_rate = 15.50
hours_worked = 40
wages = 15.50 * 40
#Calculate wages based on hourly_rate and hours_worked
print(wages)
#Print the result

hourly_rate = 15.50
hours_worked = 40
wages = hourly_rate * hours_worked
print("This week you earned: $" , wages)

#Print some maths statements
print("9 x 12 =", 9 * 12)
print("3 - 4 =", 3 - 4)
print("32 / 8=",32 / 8)
#Calculating the circumference of a circle
PI = 3.14159
diameter = 30
#Hint: The circumference of a circle is pi times the diameter
print("The circumference of the circle is:", PI * diameter)

#Calculate wages
hourly_rate = 15
hours_worked = 35
wages = hourly_rate * hours_worked
#Print out wages
print("This week you have earned: ${}".format(wages))
#Print some maths statements
print("3 x 7 ={}".format(3 * 7))
print("32 - 16 ={}".format(32 - 16))
print("256 + 128 ={}".format(256 + 128))

name = input("What is your name?")
age = input("How old are you?")
print("Hi {}, {} is nice age to be.".format(name, age))

#Ask the user for personal details
name = input("What is your name?")
age = input("How old are you?")
location = input("Where are you from?")
#Print summary of input for checking
print("This is the data you have entered: ")
print("Name: " + name)
print("Age: " + age)
print("Location: " + location)

#Ask user for address details
house_number = input("What number is your house?")
street_name = input("What street do you live on?")
address = house_number + " " + street_name
#Confirm data with user
print("Your address is: {}".format(address))
confirm = input("Are these details correct? Y/N: ")

#Gather favorites data
fave_color = input("What is your favorite color?")
fave_food = input("What is your favorite food?")
fave_music = input("Who is your favorite band/musician?")
#Combine favorites into a tasty snack e.g. Purple Metallica Pizza
print("So I guess you would love to have {} {} {} at your next party!".format(fave_color, fave_music, fave_food))

perimeter_of_rectangle = (2 * 32 + 2 * 16)
print("My hovercraft is full of eels")

import turtle
tia = turtle.Turtle()
tia.forward(50)

import turtle
tia = turtle.Turtle()
tia.forward(200)
tia.left(90)
tia.forward(200)
tia.left(90)
tia.forward(200)
tia.left(90)
tia.forward(200)

import turtle
tia = turtle.Turtle()
tia.pensize(10)
tia.color("red")
tia.forward(200)
tia.left(90)
tia.color("green")
tia.forward(200)
tia.left(90)
tia.color("yellow")
tia.forward(200)
tia.left(90)
tia.color("blue")
tia.forward(200)

import turtle
timmy = turtle.Turtle()
timmy.pensize(5)
#Move to first position
timmy.penup()
timmy.goto(10, 60)
timmy.pendown()
#Draw a purple rectangle, 120 by 50
timmy.color("purple")
timmy.forward(120)
timmy.left(90)
timmy.forward(50)
timmy.left(90)
timmy.forward(120)
timmy.left(90)
timmy.forward(50)
#Move to next position
timmy.penup()
timmy.goto(420,60)
timmy.setheading(0)
timmy.pendown()
#Draw an orange triangle with sides that are 60px long
timmy.color("orange")
timmy.forward(60)
timmy.left(120)
timmy.forward(60)
timmy.left(120)
timmy.forward(60)

#Create turtle
import turtle
tina = turtle.Turtle()
tina.color("lightGreen")
tina.pensize(8)
#Draw a light green square with yellow fill
tina.fillcolor("yellow")
tina.begin_fill()
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.left(90)
tina.forward(200)
tina.left(90)
tina.end_fill()

#Glazed donuts cost $3, filled donuts cost $4 and mini donuts cost $2
#Calculate total cost for order #1: 5 glazed, 3 filled and 6 mini donuts
order1_cost = 5 * 3 + 3 * 4 + 6 * 2
#Calculate total cost for order #2: 2 glazed, 1 filled and 10 mini donuts
order2_cost = 2 * 3 + 1 * 4 + 10 * 2
#Display order summaries
print("Order #1 comes to: ${}".format(order1_cost))
print("Order #2 comes to: ${}".format(order2_cost))

#Glazed donuts cost $3, filled donuts cost $4 and mini donuts cost $2
glazed_donut = 3
filled_donut = 4
mini_donut = 2
#Calculate total cost for order #1: 5 glazed, 3 filled and 6 mini donuts
order1_cost = 5 * glazed_donut + 3 * filled_donut + 6 * mini_donut
#Calculate total cost for order #2: 2 glazed, 1 filled and 10 mini donuts
order2_cost = 2 * glazed_donut + 1 * filled_donut + 10 * mini_donut
#Display order summaries
print("""Order #1 comes to: ${}
Order #2 comes to: ${}""".format(order1_cost, order2_cost))

# Set up price variables
ps3_game = 20
ps4_game = 45
#Order #1: 1 PS3 game and 2 PS4 games
order1_price = 1 * ps3_game + 2 * ps4_game
#Order #2: 4 PS3 games, 3 PS4 games
order2_price = 4 * ps3_game + 3 * ps4_game 
#Print out total order costs
print("Order #1 comes to: ${}".format(order1_price))
print("Order #2 comes to: ${}".format(order2_price))

# Set up price variables
ps3_game = 20
ps4_game = 45
#Ask for number of each game to be purchased
num_ps3_games = int(input("How many PS3 games?: "))
num_ps4_games = int(input("How many PS4 games?: "))
#Calculate total for each type of game
ps3_total = num_ps3_games * ps3_game
ps4_total = num_ps4_games * ps4_game
#Calculate total cost
total_cost = ps3_total + ps4_total
#Print out total order cost
print("Your order costs: ${}".format(total_cost))

num_pies = 0
print("Lisa has {} pies".format(num_pies))
num_pies += 5
print("Lisa has {} pies".format(num_pies))

