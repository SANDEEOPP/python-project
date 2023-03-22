import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    primes = []
    num = 1001
    while len(primes) < 100:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

print(generate_primes())
