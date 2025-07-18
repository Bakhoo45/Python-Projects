#encryption and decryption

import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "
key = list(chars)
random.shuffle(key)

plain_Text = input("Enter a message to Encrypt : ")
encrypt_Text = ""

for letter in plain_Text:
    index = chars.index(letter)
    encrypt_Text += key[index]

print(f"Encrypted message : {encrypt_Text}")

decrypt_Text = input("Enter a message to Decrypt : ")
plain_Text = ""

for letter in decrypt_Text:
    index = key.index(letter)
    plain_Text += chars[index]

print(f"Decrypted message : {plain_Text}")


