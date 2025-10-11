print ("Hello! what is your name?")
name = "Ahad"
print (f"Nice to meet you, {name}!")
print ("How old are you?")
age = 20
bot_age = 3
age_difference = age - bot_age
print (f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
print ("What's your favorite color?")
color = "black"
print (f"Oh {color} is a beautiful color")


#===============BOT2.py=================
# A more interactive bot that asks multiple questions and uses different input types

name = input("Hello! What is your name?")
print (f"Nice to meet you, {name}!")
age_input = input("How old are you? ")
age = int(age_input)
bot_age = 3
age_difference = age - bot_age
print (f"You are {age_difference} years older than me. I'm only {bot_age} years old!")
color_input = input("What's your favorite color?")
color = color_input
print (f"Oh {color} is a beautiful color")
