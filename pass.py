# import string library and random library all
import string 
from random import *
# set the password characters 
value = string.ascii_letters + string.digits + string.ascii_lowercase + string.punctuation

strong_pass = "".join(choice(value) for x in range(randint(8,16)))

print(strong_pass)