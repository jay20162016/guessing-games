#!/usr/bin/python

#this is the game where you pick a int and the computer guesses it.

from sys import exit
from time import sleep

num = int(eval(raw_input('what integer from 0 to 1,000 do you pick for the computer to guess??')))
if num > 1000 or num < 0:
  exit
guess = 1000
error='high'
score = 0
while True:
  if error == 'high':
    guess = guess / 2
  else:
    test = guess / 2
    guess = guess - test
    del test
  print 'guess: ',str(guess)
  if guess == num :
    print "computer's score :",str(score)
    break
  else:
    score += 1
    if guess < num:
      print 'too low'
      error = 'low'
    else:
      print 'too high'
      error = 'high'
    sleep(2)
