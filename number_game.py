import random


def game():

	secert_num = random.randint(1,100)
	num_of_guess= 5
	guess=""

	while True:
		try:
			guess = int(raw_input("Enter a number between 1 and 100\n"))
		except ValueError:
			print("{} is not a number".format(guess))
		num_of_guess-=1
		
			
		print("You have {} livies left".format(num_of_guess))
		
		if guess ==secert_num and num_of_guess !=0:
			print("You guessed right!. Number was {}\n". format(secert_num))
			break
		elif guess < secert_num and num_of_guess !=0:
			print ("Higher than {}\n".format(guess))
		elif guess > secert_num and num_of_guess !=0:
			print ("lower than {}\n".format(guess))
		elif  num_of_guess ==0:
			num_of_guess= 5
			print("The number was {}".format(secert_num))
			opt = raw_input("Game Over \n.Do you want to play again? Y/n\n")
			print(opt)
			if opt =="Y":
				game()
			elif opt =='n':
				exit()
				
			
			
		
			
			
			
		


	
		
		
	
game()
	    
