import random
import string

def random_let(count):
    for i in range(count):
        yield random.choice(string.ascii_lowercase)
for letter in random_let(5):
    print(letter)