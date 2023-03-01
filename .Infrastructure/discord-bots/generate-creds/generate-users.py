import random
import string

def generate_username(length):
    """Generate a random username"""
    char = string.ascii_lowercase + string.digits
    return 'user_'+''.join(random.choice(char) for i in range(length))

for i in range(100):
    print(generate_username(4))
