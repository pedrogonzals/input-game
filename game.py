'''
Created on Jun 23, 2013

@author: PedroG
'''
import random

secret= random.randint(1,99)
guess =0
tries =0

print "ahoy i'm the Dread Pirate Roberts, and I have a secret"
print "it is a number from 1 to 99. I'll give you 6 tries"

while guess != secret and tries < 6:
    guess=input("what's yer guess? ")
    if guess < secret:
        print "too low, ye scurvey dog"
    elif guess > secret:
        print "too high, landlubber"
       
    tries = tries + 1
    
    if guess== secret:
        print "avast ya go it : found my secret, ye did it"
    elif tries == 6:
        print "no more guesses: better luck next time, matey"
        print  " the secret number was", secret
    
 
    
    
    
    