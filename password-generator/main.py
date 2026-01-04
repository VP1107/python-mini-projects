import random
from random import randint
import string

n = int(input("How long is the Password:"))


lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
number = list(string.digits)*2
punctuation = list(string.punctuation)

all_char = lowercase + uppercase + number + punctuation

password = [random.choice(all_char) for i in range (n)]

print("".join(password))