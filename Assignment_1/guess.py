import random
y = random.randrange(1, 16, 1)
print("Try to guess the number which is between 1 and 15. You have 5 guesses allowed\n")
i = 5
while i > 0 :
	x = input("Enter guess : ")
	if int(x) < y :
		print("The Number is greater than your guess\n")
	if int(x)>y :
		print("The Number is smaller than your guess\n")
	if int(x)==y :
		print("Your Guess is Right. You win\n")
		break
	i-=1