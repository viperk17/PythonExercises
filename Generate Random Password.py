import string
import random

def GeneratePassword(size = 10, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(GeneratePassword(int(input('How many characters in your password? '))))
