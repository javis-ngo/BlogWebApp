import hashlib
import random
import string
import time


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string.lower()

def hash_password(password):
    return hashlib.sha512(password.encode('utf-8')).hexdigest()

def get_time_stamp():
    return round(time.time() * 1000)