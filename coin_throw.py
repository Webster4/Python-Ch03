# This is simulation of throw a coin
# The program counts how many times reverse and tail was drawn in 100 attempts

import random

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
		

	
throws = 1
reverse = 0
tail = 0

while throws != 101:
	score = random.randint(0, 1)
	if score:
		reverse +=1
	else: 
		tail +=1
	throws +=1
	

print("\nThe coin was thrown 100 times. The score is:",reverse, "for reverse and ",tail,"for tail")

input("\n\nPlease press enter key if you want exit")