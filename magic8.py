import random

answer1 = 'Yes - definitely.'
answer2 = 'It is decidedly so.'
answer3 = 'Without a doubt.'
answer4 = 'Reply hazy, try again.'
answer5 = 'Ask again later.'
answer6 = 'Better not tell you now.'
answer7 = 'Outlook not so good.'
answer8 = 'Very doubtful.'
answer9 = 'My sources say no.'


name = "Jake"
question = 'Will I win the lottery?'

random_number = random.randint(1, 9)
#random_number = 1

if random_number == 1:
  answer = answer1
elif random_number == 2:
  answer = answer2
elif random_number == 3:
  answer = answer3
elif random_number == 4:
  answer = answer4
elif random_number == 5:
  answer = answer5
elif random_number == 6:
  answer = answer6
elif random_number == 7:
  answer = answer7
elif random_number == 8:
  answer = answer8
elif random_number == 9:
  answer = answer9
else:
  answer = "Error"



if (not len(name) == 0) and (not len(question) == 0):
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)
elif (len(name) == 0) and (not len(question) == 0):
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
elif (question == ""):
    print("The Magic 8-Ball cannot provide a fortune unless you ask it something.")












