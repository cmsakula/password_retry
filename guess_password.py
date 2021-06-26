password = 'a123456'
tries =3
while tries != 0:
	guess = input('guess my password: ')
	if guess == password:
		print('You guess it right')
		break
	else:
		tries = tries - 1
		if tries == 0:
			print('You have no more chances!')
		else:
			print('That is wrong, you have ', tries, 'tries')
