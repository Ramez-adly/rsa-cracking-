import random
import math
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(bit_length):
    while True:
        prime = random.getrandbits(bit_length)
        if is_prime(prime):
            return prime

def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


p = generate_prime(16)     #change the bit length as u want
q = generate_prime(16)

while p == q:
    q = generate_prime(16)

n = p * q
euler_phi = (p - 1) * (q - 1)
e = random.randint(3,euler_phi-1)

while e < euler_phi:
    if extended_gcd(e, euler_phi)[0] == 1:
        gcd, x, y = extended_gcd(e, euler_phi)
        d = x % euler_phi
        break
    else:
        e += 1

print("the public key is ",e)
print("the private key is ",d)
print("the n is ", n)
print("the euler_phi is ", euler_phi)
print("p:'", p)
print("q:'", q)
print("e:", e)


message=input("enter the message you want to send ")


message_encoded= [ord(ch)for ch in message]

ciphertext=[pow(ch,e,n) for ch in message_encoded]
        
print(ciphertext)


message_decoded=[pow(ch,d,n)for ch in ciphertext]
message_="".join(chr(ch)for ch in message_decoded)

print(message)















def encrypt_message(message, public_key):
    e, n = public_key
    encrypted_message = pow(message, e, n)
    return encrypted_message

def decrypt_message(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = pow(encrypted_message, d, n)
    return decrypted_message




