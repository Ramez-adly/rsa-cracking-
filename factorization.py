import math
import time


def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def calculate_private_key(e, totient):
    start_time = time.perf_counter()
    
    gcd, x, y = extended_gcd(e, totient)
    
    if gcd != 1:
        raise ValueError("The public key is not valid.")
    
    end_time = time.perf_counter()
    runtime = (end_time - start_time)*1000
    
    return x % totient , runtime 

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

# RSA parameters
n = int(input("Enter the n of the public key: "))
e = int(input("Enter the e of the public key: "))

factors = factorize(n)

if len(factors) == 2:
    p, q = factors
    phi_N = (p - 1) * (q - 1)
    d, runtime = calculate_private_key(e, phi_N)  
    print("RSA Parameters:")
    print("p:", p)
    print("q:", q)
    print ("phi_N:", phi_N)
    print("n:", n)
    print("e:", e)
    print("d:", d)
    print("the runtime in ms is  ", runtime)  
    # Message Encryption
    message = input("Enter the message to encrypt: ")
    message_encoded = [ord(ch) for ch in message]
    ciphertext = [pow(ch, e, n) for ch in message_encoded]
    print("Encrypted Message:", ciphertext)

    # Message Decryption
    message_decoded = [pow(ch, d, n) for ch in ciphertext]
    decrypted_message = "".join(chr(ch) for ch in message_decoded)
    print("Decrypted Message:", decrypted_message)
else:
    print("N is not a product of exactly two prime numbers.")