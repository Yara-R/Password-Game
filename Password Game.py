import os
os.system("cls")

import random
import time
def jogo():
	nums = list(range(10))
	random.shuffle(nums)
	n1, n2, n3, n4 = nums[:4]

	password = str(n1) + str(n2) + str(n3) + str(n4)
	even = 0

	if n1 % 2 == 0:
		even += 1

	if n2 % 2 == 0:
		even += 1

	if n3 % 2 == 0:
		even += 1

	if n4 % 2 == 0:
		even += 1

	print("\nYou managed to access the control of the bomb!\nTo defuse it, enter the correct 4-digit password.\nYou have 60 seconds!")
	print(f"Hint: Password has {even} even number(s)\n")
	
	while True:
		guess = input("Enter a 4-digit password: ")
		present = 0

		nums = [n1, n2, n3, n4]

		if str(n1) in guess:
			present += 1
		if str(n2) in guess:
			present += 1
		if str(n3) in guess:
			present += 1
		if str(n4) in guess:
			present += 1

		if(guess[0]==password[0]):
			print("\nThe first number is right!")
		if(guess[1]==password[1]):
			print("\nThe second number is right!")
		if(guess[2]==password[2]):
			print("\nThe third number is right!")
		if(guess[3]==password[3]):
			print("\nO fourth number this is right!")

		if present == 4:
			print("\nIt is NOT over yet, to save Erick connect the red wire to the positive pole that is energized!\n")
			#a='a'
			#return(a)
			break

		elif present == 4 :
			print(f"\nAll numbers are part of the password.\n")

		else:
			print(f"\n{present} numbers are part of the password.")
