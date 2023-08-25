from euler_3 import is_prime

primes = [2]
num = 3
while len(primes) < 10001:
    if is_prime(num):
        primes.append(num)
        print(num)
    num += 2

print("prime no. 10001:", primes[-1], len(primes))
    