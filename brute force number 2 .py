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

def brute_decrypt_message(e, n, encrypted_message, plaintext):

  factors = factorize(n)  #  prime factors of n
  if len(factors) != 2:
    print("Decryption failed: Public key n requires two prime factors.")
    return None
  p, q = factors  # Assuming n has exactly two prime factors

  phi_n = (p - 1) * (q - 1)  # Calculate totient

  d = 1
  iterations = 0
  start_time = time.perf_counter()

  while True:  # Loop  until d is found
    decrypted_msg = ''
    for char in encrypted_message:
      decrypted_char = pow(char, d, n) 
    if decrypted_msg == plaintext and ((e * d) % phi_n == 1): #it takes a long time so only use (e*d% phi_n ==1 only for faster  output
      end_time = time.perf_counter()
      runtime = (end_time - start_time) * 1000
      print("Decrypted message:", decrypted_msg)
      print("Private key exponent (d):", d)
      print("Number of iterations:", iterations)
      print("Runtime:", runtime, "ms")
      return decrypted_msg

    d += 1
    iterations += 1  # Track iterations   
    
# Get user input for public key (e, n)
n = int(input("Enter the n of the public key: "))
e = int(input("Enter the e of the public key: "))

# Get user input for ciphertext (comma-separated integers)
encrypted_message_str = input("Enter the ciphertext (comma-separated integers): ")
encrypted_message = [int(x) for x in encrypted_message_str.split(',')]

# Get user input for plaintext
plaintext = input("Enter the expected plaintext message: ")

# Call the decryption function
brute_decrypt_message(e, n, encrypted_message, plaintext)
