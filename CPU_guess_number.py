#Komputer ma za zadanie zgadnąć liczbę

import random

#Powitanie
print("Witaj \nZostaniesz poproszony po podanie liczby. Zadaniem komputera będzie zgadnąć jaka to liczba")

#Podanie liczby
print("\nPomyśl liczbę od jednego do stu. Podpowiadaj komputerowi mówiąc czy liczba jest większa bądź mniejsza od pomyślanej")


min = 1
max = 100
tries = 1
guess = random.randint(min, max)
print(guess)
result = ""

while result != "OK":
	result = input("Czy Twoja liczba jest wyższa od podanej (higher) niższa (lower) czy OK? ")
	tries += 1
	if result == "higher":
		min = guess
		guess = random.randint(min, max)
		print(guess)
	elif result == "lower":
		max = guess
		guess = random.randint(min, max)
		print(guess)
	elif result == "OK":
		print(guess)
		print("Komputer zgadł liczbę w ", tries, " podejść")
	
	
print("Komputer zgadł podaną przez Ciebie liczbę. Potrzebował na to ", tries, "prób.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")