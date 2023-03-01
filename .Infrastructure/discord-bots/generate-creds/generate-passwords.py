import random
import string

def generate_username(length):
    """Generate a random password"""
    char = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    return ''.join(random.choice(char) for i in range(length))

# Generate 10 usernames of length 8
for i in range(100):
    print(generate_username(10))
