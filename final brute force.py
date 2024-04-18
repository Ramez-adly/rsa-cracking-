import time
import math

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

def brute_force_decrypt(e, n, encrypted_message):
    factors = factorize(n)  # Prime factors of n
    if len(factors) != 2:
        print("Decryption failed: Public key n requires two prime factors.")
        return None
    p, q = factors  # Assuming n has exactly two prime factors
    phi_n = (p - 1) * (q - 1)  # Calculate totient

    d = 1
    iterations = 0
    start_time = time.perf_counter()

    while True:
        iterations += 1
        if (e * d) % phi_n == 1:
            end_time = time.perf_counter()
            runtime = (end_time - start_time) * 1000

            decrypted_msg = ''
            for char in encrypted_message:
                decrypted_char = pow(char, d, n)
                decrypted_msg += chr(decrypted_char)

            print("Decrypted message:", decrypted_msg)
            print("Private key exponent (d):", d)
            print("Number of iterations:", iterations)
            print("Runtime:", runtime, "ms")
            return decrypted_msg

        d += 1

# Get user input for public key (e, n)
n = int(input("Enter the n of the public key: "))
e = int(input("Enter the e of the public key: "))

# Get user input for ciphertext (comma-separated integers)
encrypted_message_str = input("Enter the ciphertext (comma-separated integers): ")
encrypted_message = [int(x) for x in encrypted_message_str.split(',')]

# Call the decryption function with n, e, and encrypted_message
decrypted_message = brute_force_decrypt(e, n, encrypted_message)

# Print the decrypted message only if decryption was successful
if decrypted_message:
    print("Decrypted message:", decrypted_message)
