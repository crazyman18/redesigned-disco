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

#Here they put the info
age = int(input("How old are you?"))
years_to_add = int(input("How many years you would like to add?"))
#Increment
age += years_to_add
print("In {} years you will be {}".format(years_to_add, age))

#Set up variables
number1 = 35
number2 = 7
number3 = 16
#Change variables
number1 -= 10
print(number1)
number2 *= 4
print(number2)
number3 /= 8
print(number3)

# Set up price variables
ps3_game = 20
ps4_game = 45
#Temporary discount on PS3 games
ps3_game -= 2
#Ask for number of each game to be purchased
num_ps3_games = int(input("How many PS3 games?: "))
num_ps4_games = int(input("How many PS4 games?: "))
#Calculate total for each type of game
ps3_total = num_ps3_games * ps3_game
ps4_total = num_ps4_games * ps4_game
#Calculate total cost
total_cost = ps3_total + ps4_total
#Apply 15% discount
total_cost *= 0.85
#Print out total order cost
print("You order costs: ${}".format(total_cost))

print("A computer programmer can earn 6 figures!")
print("She looked up and yelled \"Watch out! You'll break it!\"")
number = int(input("What's your favorite number?"))
print("Your favorite number is: {}".format(number))

print(3 + 2 * (5 ** 2))
shoe_size = int(input("What size are your shoes?"))
print("My shoes are twice as big, they are size {}".format(shoe_size * 2))

catch_phrase1 = "Ni!"
catch_phrase2 = "Ekki-ekki-ekki-pitang-zoom-boing!"
print("We are the knights who say {}".format(catch_phrase1))
print("Erm, wait a minute...")
print("We are no longer the knights who say {}, we are the knights who say {}".format(catch_phrase1, catch_phrase2))

donut_price = 5
#Ask how many donuts
num_donuts = int(input("How many gourmet donuts would you like? "))
#Calculate price and apply Super Saturday discount
print("But wait! It's Saturday so you get $1 off your total order for each donut purchased!")
order_total = num_donuts * donut_price - num_donuts
#Display order total
print("That will cost: ${}".format(order_total))

# Ask and greet by name
name = input("What is your name?")
print("Hello {}!  Let's work out what you earned this week".format(name))
#Ask user for work data
hourly_rate = int(input("How much do you earn per hour?"))
hours_worked = int(input("How many hours do you work per day?"))
days = int(input("How many days per week do you work?"))
#Calculate wages for the week
wages = hourly_rate * hours_worked * days
print("Your pay this week before tax is: ${}".format(wages))
#Take off 20% tax
wages *= 0.8
print("After tax @ 20% that is: ${}".format(wages))

name = input("What is your name?")
print(name)
birth = int(input("What year you were born?"))
age = 2020 - birth
print("You will be {} years old this year!".format(age))

# Add 4 to 8 and then divide by 2
print((4 + 8) / 2)
#Increase score
score = 5
score += 10
print(score)
#Calculate area of a rectangle
length = 120
width = 75
print("The area of the rectangle is {}".format(length * width))
#Ask the user for 2 numbers and store them as variables.  Don't forget int()!
num1 = int(input("What is the first number"))
num2 = int(input("What is the second number"))
#Print out the sum of the 2 numbers (just by itself, without a sentence)
print(num1 + num2)

string1 = "The quick brown fox "
string2 = "jumps over the lazy dog"
#Combine the strings
print(string1 + string2)
#Print Coding is fun! 8 times
print("Coding is fun!" * 8)
#Add the calculation
print("27 / 3 = ", 27 / 3)
#Include the phone number
phone = "0211234567"
print("This number:{} is a mobile phone number".format(phone))

print('"Python" is a cool programming language')
print("Monty Python is very funny. You should watch it!")
#Create variables
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = first_name + " " + last_name
print("Your first name is: {}, your last name is: {} and together that makes you: {}".format(first_name, last_name, full_name))

name = input("What is your name?")
if name == "Samuel":
  print("That's a pretty cool name!")
else:
  print("Not as cool as my name!")
  
print(4 == 9)
print("Bob" == "Bob")
#Write a print statement that evaluates to True
print(1 == 1)
#Write a print statement that evaluates to False
print("Samuel" == "Cool")

#Print statement practice
print(5 < 35)
print(3 * 3 > 4 * 4)
#Getting some user input
number = int(input("Pick a number"))
if number < 10:
  print("You picked a low number, less than 10 in fact")
else:
  print("Your number is greater than or equal to 10")

number = int(input("Pick a number: "))
if number <= 10:
  print("That's a small number!")
elif number > 10 and number <= 100:
  print("That's a medium sized number")
else:
  print("Wow that's big!")

#Ask the user how they feel
mood = input("How are you feeling today?")
#Print a response depending on their mood
if mood == "happy":
  print("That's great!")
elif mood == "sad":
  print("Sorry to hear that")
elif mood == "tired":
  print("You should get an early night")
else:
  print("Oh, really?")
fave_food = input("What is your favorite food?")
if fave_food == "pizza":
  print("Me too!")

# Make these print statements print True
print("Sarah" == "Sarah")
print("Pizza is very cheesy" == "Pizza is very cheesy")
# Make these print statements print False
print("Ni!" == "ni!")
print("Learn to Code; change the world" == "learn to Code; change the world")

.strip() #removes all spaces from the start and end of the string.
.lower() # converts a whole string to lower case
.upper() # CONVERTS A WHOLE STRING TO UPPER CASE
.title() # Gives Each Word A Capital
.capitalize() # Makes the first letter of the string a capital

word = input("Enter a word: ")
# Changing to lower case
word = word.lower()
print(word)
# Strip spaces and print
word = word.strip()
print(word)
# Change to title case and print
word = word.title()
print(word)
# Change to upper case and print
word = word.upper()
print(word)

#Ask the user for their height
height = int(input("Enter your height in cm: "))
#Tell them if they are short or tall
if height > 165:
  print("You are tall")
else: 
  print("You are short")

#Ask user how long they spend online
online_time = int(input("How long you spend online?"))
#Check if they spend too much time or not
if online_time < 3:
  print("That's a healthy amount of time")
else:
  print("You need to get more fresh air!")

#Ask user how long they spend online
internet_hours = int(input("How many hours do you spend on the internet each day? "))
#Check if they spend too much time or not
if internet_hours < 3 and internet_hours > 1:
  print("That's a healthy amount of time")
elif internet_hours >= 3 and internet_hours <= 5:
  print("Make sure you are also being active.")
elif internet_hours > 5 and internet_hours <= 24:
  print("You need to get more fresh air!")
else:
  print("There are only 24 hours in a day!")
  
#Set the correct answer to 9
#Constant Variables are when they are all in upper case
ANSWER = 9
#Ask the user to guess the number
guess = int(input("What number am I thinking of? "))
#Check if they are right or not
if guess == 9:
  print("Correct!")
else:
  print("Nope, you are wrong!") 

ANSWER = 9
#Ask user for their guess
guess = int(input("Guess a number: "))
#Check if they are correct
if guess == ANSWER:
  print("You chose: {}".format(guess))
  print("Analysing...")
  print("You are correct!")
else:
  print("You chose: {}".format(guess))
  print("You are incorrect...")
  print("Better luck next time!")

weight = int(input("How much does your parcel weigh? "))
# Check the weight variable
if weight > 0 and weight <= 3:
  print("Shipping will cost $5")
elif weight > 3 and weight <= 10:
  print("Shipping will cost $10")
else:
  print("Contact us for a quote")

DELIVERY = 10
PIZZA_PRICE = 15
# Set variable equal to input
num_pizzas = int(input("How many pizzas do you want?"))
#Set variable to pizzas times price
order_total = num_pizzas * pizza_price
# if pizzas are less than 3
if num_pizzas < 3:
  print("Delivery will cost ${}".format(delivery))
  order_total += delivery
else:
  print("Free delivery for 3 or more pizzas!")
#Print "Your order comes to:..."
print("Your order comes to: ${}".format(order_total))

print("Education is the {2} to unlock the golden {0} of {1}. -George Washington Carver".format("door","freedom","key"))
word1 = "Knowledge"
word2 = "Wisdom"
print("{1} is knowing a tomato is a fruit. {0} is not putting it in a fruit salad.".format(word2, word1))

print("By all means let's be {0}, but not so {0} that our brains drop out.".format("open-minded"))
print("We are no longer the Knights who say \"{2}!\", we are the Knights who say \"{1}-{1}-{1}-{0}-{3}-boing!\"".format("pitang","ekki","ni","zoom"))

#Set up the sentence skeleton
SENTENCE = "I {} the {} {}"
#Ask user for words to put in sentence
verb = input("Please enter a verb (doing word): ")
adj = input("Please enter an adjective (describing word): ")
noun = input("Please enter a noun (thing): ")
#Print out sentence.
print(SENTENCE.format(verb, adj, noun))

HOURLY_RATE = 13.75
hours_worked = 37.5
wages = HOURLY_RATE * hours_worked
print("This week you worked: {:.1f} hours".format(hours_worked))
print("You earned: ${:.2f} before tax".format(wages))
#Take off 20% tax
wages *= 0.8
#Add your print statement here
print("After tax: ${:.2f}".format(wages))

score = 0
#Ask the next question
answer = input("Which metal is heavier, silver or gold?")
answer = answer.strip().lower()
#Check if answer is correct and add or remove points
if answer == "gold":
  print("That is correct, you get 10 points!")
  score += 10
else:
  print("Sorry, that is incorrect, you lose 2 points")
  score -= 2
print("Your score is now: {} points".format(score))
#Ask the next question
answer = input("Ganymede is a moon of which planet?")
answer = answer.strip().lower()
#Check if answer is correct and add or remove points
if answer == "jupiter":
  print("That is correct, you get 5 points!")
  score += 5
else:
  print("Sorry, that is incorrect, you lose 3 points")
  score -= 3
print("Your score is now: {} points".format(score))
#Ask the next question
answer = int(input("How many bees does it take to equal approximately the same weight as one M&M candy?"))
#Check if answer is correct and add or remove points
if answer == 10:
  print("That is correct, you get 100 points!")
  score += 100
elif answer > 10:
  print("The answer is lower! You lose 20 points")
  score -= 20
elif answer < 10:
  print("The answer is higher! You lose 20 points")
  score -= 20
print("Your score is now: {} points".format(score))
#Ask the next question
answer = input("What is the name of Saturn's largest moon?")
answer = answer.strip().lower()
#Check if answer is correct and add or remove points
if answer == "titan":
  print("That is correct, you get 10 points!")
  score += 10
elif answer == "ganymede":
  print("You're thinking of Jupiter! You lose 5 points")
  score -= 5
else:
  print("Sorry, incorrect, You lose 5 points")
  score -= 5
print("Your score is now: {} points".format(score))

# Write your code here
icecream_flavor = input("What is your favorite ice cream flavor")
icecream_flavor = icecream_flavor.strip().lower()
if icecream_flavor == "cookies and cream":
  print("Mine too!")
#Write your code here
fruit_servings = int(input("How many servings of fruit and vegetables you had today?"))
if fruit_servings >= 5:
  print("Well done, you've had your 5+ today!")
else:
  print("You should eat 5+ a day, every day.")
#Write your code here
movie_rate = int(input("Rate the last movie you watched out of 5?"))
if movie_rate == 3:
  print("Pretty average huh?")
elif movie_rate < 3:
  print("Wow, that must have been bad!")
elif movie_rate > 3 and movie_rate <= 5:
  print("Sounds like a great movie!")
else:
  print("I said out of 5!")

for i in range(10):
  print(i)
print("-------- Loop 1 -------")
for i in range(0, 7):
  print(i)
print("-------- Loop 2 -------")
for i in range(1, 11):
  print(i)
print("-------- Loop 3 -------")
for i in range(20, 28):
  print(i)
print("-------- Your loop -------")
for i in range(5, 18):
  print(i)

i = 1
while i <= 10:
  print(i)
  i += 1
#Set up the variable that will run the loop
response = "no"
#Repeat loop until we are there!
while response != "yes":
  response = input("Are we there yet?")
print("Yay!")

# Print numbers 0 - 8
for i in range(9):
  print(i)
# Print "I will practice coding every day!" 5 times
for i in range(5):
  print("I will practice coding every day!")
# Give yourself 3 cheers
for i in range(3):
  print("Hip hip...")
  print("Hooray!")
#Print numbers 1-10
for i in range(1, 11):
  print(i)
print() # Don't edit this one - it's just to put a gap between your loops!
#Print numbers 20-35
for i in range(20, 36):
  print(i)
print() # Don't edit this one - it's just to put a gap between your loops!
#Print numbers 9-18 in a sentence
for i in range(9, 19):
  print("The next number is {}".format(i))
print("------- Loop #1 --------")
for i in range(0, 20, 2):
  print(i)
print("------- Loop #2 --------")
for i in range(6, 22, 3):
  print(i)
print("------- Loop #3 --------")
for i in range(10, 0, -1):
  print(i)
print("------- Loop #4 --------")
for i in range(100, -1, -10):
  print(i)
#Print 3 times table
for i in range(1, 13):
  print("3 x {0} = {1}".format(i, i*3))

#Set up turtle
import turtle
tiny = turtle.Turtle()
tiny.pensize(5)
#Draw a square using a for loop
for i in range(4):
  tiny.forward(150)
  tiny.right(90)

#Set up turtle
import turtle
tiny = turtle.Turtle()
tiny.pensize(5)
#Make a list of colors
colors = ["red", "yellow", "blue", "green"]
#Draw a square with one side each color using a loop
for color in colors:
  tiny.pencolor(color)
  tiny.forward(150)
  tiny.right(90)

#Set up turtle
import turtle
tiny = turtle.Turtle()
tiny.pensize(5)
#Go to position 
tiny.penup()
tiny.goto(60, 220)
tiny.pendown()
#Draw a red hexagon
tiny.pencolor("red")
for i in range(6):
  tiny.forward(100)
  tiny.left(60)
#Go to position
tiny.penup()
tiny.goto(360, 220)
tiny.pendown()
#Draw a triangle that has a blue line and yellow fill
tiny.fillcolor("yellow")
tiny.pencolor("blue")
tiny.begin_fill()
for i in range(3):
  tiny.forward(100)
  tiny.left(120)
tiny.end_fill()
#Go to position
tiny.penup()
tiny.goto(200, 440)
tiny.pendown()
#Draw a filled pink pentagon
tiny.fillcolor("pink")
tiny.pencolor("pink")
tiny.begin_fill()
for i in range(5):
  tiny.forward(100)
  tiny.left(72)
tiny.end_fill()

#Set up turtle
import turtle
spiro = turtle.Turtle()
spiro.color("blue")
#Draw a spirograph
for i in range(100):
#Change colors
  if i == 20:
    spiro.color("red")
  if i == 40:
    spiro.color("orange")
  if i == 60:
    spiro.color("yellow")
  if i == 80:
    spiro.color("green")
#Draw the spirograph
spiro.forward(200)
spiro.left(184)
spiro.forward(40)
spiro.right(30)
  
#Set up - always do all imports together at the top of your code
import random
import turtle
spiro = turtle.Turtle()
spiro.pensize(2)
spiro.goto(100,250)
#Change colors
red = random.randrange(0, 256)
green = random.randrange(0, 256)
blue = random.randrange(0, 256)
spiro.color((red, green, blue))
#Draw a spirograph
for i in range(100):
  spiro.forward(300)
  spiro.left(184)

#Ask the user's name and greet them
name = input("What is your name?")
print("Hello, {}!".format(name))

#Ask the user's name and greet them
name = input("What is your name?")
print("Hello, {}!".format(name))
#Ask the user for number of hours spent online for each of the past 7 days
for i in range(1, 8):
  hours = input("How many hours did you spend online on day {}?: ".format(i))
  print(hours)

#Ask the user's name and greet them
name = input("What is your name?")
print("Hello, {}!".format(name))
total_hours = 0
#Ask the user for number of hours spent online for each of the past 7 days
for i in range(1, 8):
  hours = float(input("How many hours did you spend online on day {}?: ".format(i)))
  total_hours += hours
print("You spent {:.1f} hours online in total.".format(total_hours))

#Ask the user's name and greet them
name = input("What is your name?")
print("Hello, {}!".format(name))
total_hours = 0
lowest_hours = None
#Ask the user for number of hours spent online for each of the past 7 days
for i in range(1, 8):
  hours = float(input("How many hours did you spend online on day {}?: ".format(i)))
  total_hours += hours  
#Check if current hours are the lowest hours and store if so
  if lowest_hours == None or hours < lowest_hours:
    lowest_hours = hours  
print("You spent {} hours online in total.".format(total_hours))
print("The least time you spent online in one day was {:.1f} hours".format(lowest_hours))

#Print numbers 0 - 8
i = 0
while i < 9:
  print(i)
  i += 1
# Print "I will practice coding every day!" 5 times
i = 0
while i < 5:
  print("I will practice coding every day!")
  i += 1
# Give yourself 3 cheers
i = 0
while i < 3:
  print("Hip hip")
  print("Hooray")
  i += 1

#Print numbers 1-5
i = 1
while i <= 5:
  print(i)
  i += 1
print()
#Print numbers 10-25
i = 10
while i <= 25:
  print(i)
  i += 1
print()
#Print numbers 9-18 in a sentence
i = 9
while i <= 18:
  print("The next number is {}".format(i))
  i += 1

print("------- Loop #1 --------")
i = 1
while i <= 128:
  print(i)
  i *= 2
print("------- Loop #2 --------")
i = 6
while i <= 21:
  print(i)
  i += 3
print("------- Loop #3 --------")
i = 10
while i > 0:
  print(i)
  i -= 1
print("------- Loop #4 --------")
i = 100
while i >= 0:
  print(i)
  i -= 10

#Print 3 times table
i = 1
while i <= 12:
  print("3 x {} = {}".format(i, i * 3))
  i += 1

# Set a correct answer
ANSWER = 9
# Give the user 3 lives
lives = 3
# Give the user 3 tries to guess the number, and tell them whether they are correct or not
while lives > 0:
  guess = int(input("Guess the number i am thinking of: "))
  if guess == ANSWER:
    print("Correct!")
    lives = 0
  else:
    print("Wrong!")
    lives -= 1

# Set amount of pocket money
pocket_money = 40.00
#Ask the user for the price of items until they can't afford anymore
while pocket_money > 0:
  price = float(input("What price do you want to buy?"))
  pocket_money -= price
  print("You have ${:.2f} left".format(pocket_money))

# Set amount of pocket money
pocket_money = 40.00
still_shopping = True
#Ask the user for the price of items until they can't afford anymore
while still_shopping == True:
  price = float(input("How much do you want to spend on this item? "))
  pocket_money -= price
  print("You have ${:.2f} left".format(pocket_money))
  #Check if the user wants to purchase more
  confirm = input("Would you like to keep shopping?")
  if confirm == "no":
    still_shopping = False

# Set amount of pocket money
pocket_money = 40.00
still_shopping = True
#Ask the user for the price of items until they can't afford anymore
while still_shopping == True and pocket_money > 0:
  price = float(input("How much do you want to spend on this item? "))
  #Check if they have enough for that item
  if price <= pocket_money:
    pocket_money -= price
  else:
    print("You can't afford that")
  print("You have ${:.2f} left".format(pocket_money))
  #Check if the user wants to purchase more
  confirm = input("Would you like to keep shopping? ")
  if confirm == "no":
    still_shopping = False

#Ask user how long they have exercised for today
time = int(input("How many minutes of exercise you did today?"))
#If an invalid number is entered, repeat until they enter one between 0-1440
while time < 0 or time > 1440:
  print("Please enter a valid number. The total minutes in one day is 1440")
  time = int(input("How many minutes of exercise you did today?"))

#Break this loop after 13 is printed  
for i in range(5, 15):
  print(i)
  if i == 13:
    break     
print("-----") #Separate the output from the 2 loops
#Make this loop skip printing 9
for i in range(12):
  if i == 9:
    continue
  print(i)

# Ask user for login details and give them 3 tries
PASSWORD = "ekki-ekki-ekki"
for i in range (3):
  guess = input("Password: ").strip().lower()
  if guess == PASSWORD: # If correct
    print("Correct, authorisation complete.")
    break
  else: #If incorrect
    print("Incorrect")    
else: #If incorrect 3 times
  print("Sorry, 3 incorrect guesses, your account has been locked.")

# Force the user to choose a valid option
while True:
  answer = input("True or false? Sharks are mammals: ").strip().lower()
  #Exit loop if user has entered a valid answer
  if answer == "true" or answer == "false": 
    break
  else: #Tell them to enter a valid answer
    print("Please answer with true or false")
#Go on to check if they were right or wrong

#Force the user to enter a valid number
while True:
  try:
    height = float(input("Enter your height in metres: "))
    break
  except ValueError:
    print("Please enter a valid height in metres e.g. 1.65")

# Ask the user for number of hours spent exercising, this accepts expected values
while True:
  try:
    hours = float(input("How many hours did you spend exercising today?: "))
    if hours < 0 or hours > 24:
      print("Please enter a number from 0-24!")
    else:
      break
  except ValueError:
    print("Please enter a valid number!")  
print("You spent {:.1f} hours exercising today.".format(hours))

#Give the user 5 tries to guess a number
NUMBER = 4
GUESSES = 5
for i in range(GUESSES):
  print("You have {} guesses left.".format(GUESSES - i))
  guess = int(input("Guess the number: "))  
  if guess == NUMBER:
      print("Yes! That's right!")
      break
  else:
      print("Wrong!")
else:
  print("Out of guesses, the answer was {}!".format(NUMBER))

#Ask the user to choose a number between 1 and 10
number = int(input("Choose a number between 1 and 10: "))
while number < 1 or number > 10:
  print("Please enter a number between 1 and 10!")
  number = int(input("Choose a number between 1 and 10: "))
print("You chose: {}.".format(number))

#Print "I must do my homework!" 10 times
i = 0
while i < 10:
  print("I must do my homework!")
  i += 1  
#Print the numbers 10 to 1 counting down
i = 10
while i > 0:
  print(i)
  i -= 1

#Ask the user to enter the number of hours sleep they got last night. This should accept values between 0 and 24 inclusive, and force the user to re-enter if they enter invalid data.
while True:
  try:
    sleep_hours = float(input("How many hours sleep did you get last night?"))
    if sleep_hours < 0 or sleep_hours > 24:
      print("You can't sleep negative hours, or more than 24 hours in one day!")
    else:
      break
  except ValueError:
    print("Please enter a number.")
#Check if they are getting enough sleep
if sleep_hours >= 12:
  print("Wow, that's a lot of sleep!")
elif sleep_hours < 12 and sleep_hours >= 8:
  print("You got enough sleep last night")
else:
  print("You should try to get more sleep!")

#For loop
for i in range(2, 19):
  print(i)
#While loop
i = 2
while i < 19:
  print(i)
  i += 1

# Ask user to enter sleep data for day 1 through to day 7
for i in range(1, 8):
  hours_sleep = int(input("Enter hours of sleep on day {}: ".format(i)))
  print("Hours of sleep on day {}: {}".format(i, hours_sleep))
#Print out 1 - 3 times tables
for i in range(1, 4):
  for j in range(1, 4):
    print("{} x {} = {}".format(i, j, i * j))    

#For loop
maximum = int(input("Pick a number:"))
for i in range(0, maximum):
  print(i)
#While loop
answer = input("What is the coolest programming language?").strip().lower()
while answer != "python":
 answer = input("What is the coolest programming language?").strip().lower()
