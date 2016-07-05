# this is the game in which you guess the int.
import random

choice = int(raw_input('up to what number'))
num = random.randint(0,choice)
score = 0
print 'you want your score to be lowest'

while True:
  guess = int(raw_input("whats's your guess"))
  if guess == num :
    print 'correct!!!!! your score is ',score
    print 'you want your score to be lowest'
    giveup = raw_input('do you give up??')
    if giveup == 'yes' :
      break
    else :
      score = 0
      guess = int(raw_input("whats's your guess"))
      num = random.randint(0,choice)
  else:
    if score > num :
      print 'too high'
    else :
      print 'too low'

