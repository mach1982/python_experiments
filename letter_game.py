import random
import os
import sys

#Create list of words


words= [
	'dog', 
	'computer', 
	'house',
	'car',
	'rasberry',
	'lemon'
	]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def draw(bad_guess,good_guess,s_word):
	clear()
	print(bad_guess)
	
	for letter in bad_guess:
		print(letter,end=' ')
	print('\n\n\n')
		
	
	for letter in s_word:
		if letter in good_guess:
			print(letter,end=' ')
				
		else:
			print('_',end=' ')
	print('')
	

def get_guess(bad_guess,good_guess):
	while True:
		guess = input('Guess a letter:').lower()
		
		if len (guess) !=1:
			print('You can only guessa singel letter')
		elif guess in bad_guess or guess in good_guess:
			print ("You have already guess that letter")
		elif not guess.isalpha():
			print("Guess was nota letter")
		else:
			return guess
				
				

def play(done):
	clear()
	s_word = random.choice(words)	
	good_guess=[]
	bad_guess=[]
	
	
	while True:
		draw(bad_guess,good_guess,s_word)
		guess =get_guess(bad_guess,good_guess)
		
		if guess in s_word:
			good_guess.append(guess)
			found=True
			for letter in s_word:
				if letter not in good_guess:
					found=False
				
			if found:
				print("You win.\n The Word was {}".format(s_word))
				done =True
				
		if done	:
			play_again = input("Play again? Y/n").lower()
			if play_again != 'n':
				return play(done=False)
			else:
				sys.exit()
				
		
		
def welcome():
	print("Welcom to the letter game")
	start=input("Press Enter/Return to start or enter Q to quit")
	if start.lower() == 'q':
		print("bye")
		sys.exit()
	else:
		return True
	

	
done=False
	
while True:
	clear()
	welcome()
	play(done)
		
	
			
			
	
		
		
 
