import random
import string

# define this variable as per the requirement
length_of_password = 12

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length_of_password)

password = "".join(temp)

print(password)