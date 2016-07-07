#!/usr/bin/python

# this is the game in which you guess the integer.
#type num to cheat


import random

choice = int(eval(raw_input('up to what number??')))
num = random.randint(0,choice)
score = 0
print 'you want your score to be lowest.'

while True:
  guess = int(eval(raw_input("whats's your guess??")))
  if guess == num :
    print 'correct!!!!! your score is ',str(score)
    print 'you want your score to be lowest.'
    giveup = raw_input('do you give up??')
    if giveup == 'yes' :
      break
    else:
      choice = int(eval(raw_input('up to what number??')))
      num = random.randint(0,choice)
      score = 0
  else:
    if score > num :
      print 'too high'
    else :
      print 'too low'
    score += 1
