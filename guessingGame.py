import random

highest = 7
answer = random.randint(1, highest)
guess = int(input("Guess a number between 1 and {}: ".format(highest)))

while guess != answer:
	if (guess == 0) or (guess > highest):
		guess = int(input("Outside of specified range, guess again: "))
	elif guess < answer:
		guess = int(input("Too low, guess a bigger number: "))
	else:
		guess = int(input("Too high, guess a smaller number: "))
else:
	print("You guessed it!!")