print ("Hello, Samuel!")

print ("""How are you...
Are you Fine...
Are you Good..""")

print ("How are you...\nAre you Fine...\nAre you Good..")

print (5, 3)
print (5 + 3)
print (5 - 3) #practice in phyton
print (5 / 3)
print (5 * 3)

print ("Hello" + "Samuel")
print ("HelloSamuel" * 3)

name = input("What is your name?")
print(name)
age = input("What is your age?")
print(age)
print (name, age)

a = 5
print (a)
price =15.50
print (price)

name = input("What is your name?")
age = input("How old are you?")

print("{} is a nice age to be, {}!".format(age, name))

name = input("What is your name?")
color = input("What is your favorite color?")
food = input("What is your favorite food?")

print("Well then {}, I bet you'd love {} {} then!".format(name,color,food))

age = int(input("How old are you?"))
print("In 10 years you will be {}".format(age + 10))

siblings = int(input("How many brothers and sisters do you have?"))
total_children = siblings + 1

print("That means your parents have {} children in total.".format(total_children))

number = 10
number += 5 # Adds 5, number is 15
number -= 5 # Subtracts 5, number is 10 again
number *= 5 # Multiplies by 5, number is 50
number /= 5 # Divides by 5, number is 10 again
print (number)

number = 2
number += 3
number *= 10
number /= 5
number += number
print (number)

age = int(input("How old are you?"))

if age <= 12:
  print("You are a child")
elif age > 12 and age < 20:
  print("You are a teen")
elif age < 0 or age > 125:
  print("Invalid age")
else:
  print("You are an adult")

food = input("What is your favorite food?")

if food == "pizza":
  print("Yum!")
