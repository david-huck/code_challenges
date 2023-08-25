from euler_3 import is_prime

prim_sum = 2
for i in range(3,2_000_000,2):
    if is_prime(i):
        prim_sum += i

print(prim_sum)