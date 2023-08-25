def square_sum(upper):
    return sum([i**2 for i in range(upper)])
def sum_square(upper):
    return sum([i for i in range(upper)])**2

upper = 100

diff = sum_square(101) - square_sum(101)

print(diff)