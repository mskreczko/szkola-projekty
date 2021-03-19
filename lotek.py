import random
import sys


try:
	max_tries = int(input("Ile prob maksymalnie chcesz miec: "))

	print("W jakim zakresie chcesz szukac liczb: ")
	min_range = int(input("Zakres dolny: "))
	max_range = int(input("Zakres gorny: "))

	number = random.randint(min_range, max_range)
	print(number)
except ValueError:
	print("Podales niepoprawna wartosc! Upewnij sie ze uzywasz liczb")
	sys.exit(0)

n_tries = 0

while True:
	guess = int(input("Wprowadz liczbe: "))
	if guess > max_range or guess < min_range:
		print("Podales liczbe z poza zakresu!")
		continue

	if number == guess:
		print("Brawo! Zgadles za {} razem".format(n_tries+1))
		break
	else:
		print("Pudlo")
		n_tries += 1
		if n_tries == max_tries:
			print("Przegrales, skonczyly ci sie proby")
			break
