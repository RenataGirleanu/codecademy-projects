import random
name = "Renata"
question = "Is my name Renata?"
answer = ""

random_number = random.randint(1, 9)
print(random_number)

if random_number == 1:
  answer = "Yes - definetely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

if question == "":
  print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")  
else:
  
  if name == "":
    print("Question: " + question)
  else: print(name + " asks: " + question)
  
print("Magic 8-Ball's answer: " + answer)





