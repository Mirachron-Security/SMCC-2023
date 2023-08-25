import random
import string

def generate_creds(length):
    chars_user = string.ascii_lowercase + string.digits
    chars_pass = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    
    user = 'user_' + ''.join(random.choice(chars_user) for i in range(round(length/2-1)))
    password = ''.join(random.choice(chars_pass) for i in range(length))
    line = user + ' : ' + password
    return line

# Generate x pairs of creds
for i in range(10):
    print(generate_creds(10))
