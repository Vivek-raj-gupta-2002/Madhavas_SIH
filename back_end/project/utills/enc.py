import random
import string

def generate_key():
    chars = string.punctuation + string.digits + string.ascii_letters
    key = list(chars)
    random.shuffle(key)
    return key

def encrypt_message(plain_text, key):
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text

def decrypt_message(cipher_text, key):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = generate_key()
