# Symulacja rzutu monetą
# Komputer zlicza ile razy wypadł orzeł a ile reszka

import random

print("Program rzuci 100 razy monetą i wyliczy ile razy wypadła reszka, a ile orzeł")

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
	
print("\nProgram rzucił monetą 100 razy. Orzeł wypadł ", reverse, " razy, a reszka ", tail, " razy.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")