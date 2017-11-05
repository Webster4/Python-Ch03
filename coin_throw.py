# This is simulation of throw a coin
# The program counts how many times reverse and tail was drawn in 100 attempts

import random

# Function displays introduction to program
def intro():
	print("Hello in throw a coin simulation")
	print("\nComputer will throw a coin 100 times and counts how many times reverse and tail was drawn")

# This receive as parameters throw, tail and reverse counters
# It returns how many times both sides of coin were drawn
def throw_counter(throws = 1, tail = 0, reverse = 0):
	while throws != 101:
		score = random.randint(0, 1)
		if score:
			reverse +=1
		else: 
			tail +=1
		throws +=1
	return tail, reverse

# Function returns a response yes or no on question in calling 
def ask_yes_no(question):
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response

# Function asks player if he/she wants to play again
def again():
	if_again = ask_yes_no("\nDo you want play again (press y or n) ")
	if if_again == "y":
		print("\n\n")
		main()
	elif if_again == "n":
		input("\n\nPlease press enter key if you want exit\n\n")

# Function print the final result
def result(tail, reverse):
	print("\nThe coin was thrown 100 times. The score is:",reverse, "for reverse and ",tail,"for tail")
	
	
	
def main():
	intro()
	tail, reverse = throw_counter()
	result(tail, reverse)
	again()
	
# Starting of program
main()