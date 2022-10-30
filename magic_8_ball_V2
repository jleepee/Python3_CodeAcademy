#Random number module import
import random

#Base Variables
name = 'Jake'
question = ''
magic_8_answer: ''

#Generate Random number 1-9
random_number = random.randint(1,9)

#Assign random number to answer
if random_number == 1:
  magic_8_answer = 'Yes - definitely.'
elif random_number == 2:
  magic_8_answer = 'It is decidedly so.'
elif random_number == 3:
 magic_8_answer = 'Without a doubt.'
elif random_number == 4:
  magic_8_answer = 'Reply hazy, try again.'
elif random_number == 5:
 magic_8_answer = 'Ask again later.'
elif random_number == 6:
 magic_8_answer = 'Better not tell you now.'
elif random_number == 7:
  magic_8_answer = 'My sources say no.'
elif random_number == 8:
 magic_8_answer = 'Outlook not so good.'
elif random_number == 9:
  magic_8_answer = 'Very doubtful.'

#Print statement: If name and question blank print Error, if name blank print question, if question blank print need to ask question. 
if len(name) != 0 and len(question) != 0:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + magic_8_answer)
elif len(name) == 0 and len(question) != 0:
  print('Question: ' + question)
  print("Magic 8-Ball's answer: " + magic_8_answer)
elif len(name) != 0 and len(question) == 0:
  print(name + ' you need to ask a question')
elif len(name) == 0 and len(question) == 0:
  print('Please provide name and question for the Magic 8-ball')
