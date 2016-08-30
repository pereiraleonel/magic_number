def magic_number():
	magic_number = random.randrange(0,10)
	user_number = input("Enter a number (0-10):")
	if user_number == magic_number:
		print("Congratulation. you chose the magic number {}".format(user_number))
	else:
		print("Sorry. {} is not the magic number but {}".format(user_number, magic_number))
