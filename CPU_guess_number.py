#Komputer ma za zadanie zgadnąć liczbę

import random

#Welcome and intruct
print("HELLO!!! \nPlease think about some number in range from 1 to 100. Computer will try to guess the number")
print("Give a clues to computer if guess number is higher or lower than your\n\n")


# Function which takes tries counter 
def guessing(tries = 1):
	min = 1
	max = 100
	guess = random.randint(min, max)
	print(guess)
	result = None
	while result != "OK":
		result = input("\n\nYour number is higher than given by computer, lower or OK? ")
		if result == "higher":
			min = guess
			guess = random.randint(min, max)
			print(guess)
		elif result == "lower":
			max = guess
			guess = random.randint(min, max)
			print(guess)
		elif result == "OK":
			print("\nComputer guessed your number in",tries,"attempts")
		tries += 1

guessing()



input("\n\nPlease press enter key if you want exit\n\n")