
def fib(limit):
    fibs = [1,2]
    while fibs[-1] <= limit:
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

if __name__ == "__main__":
    fibonaccis = fib(4_000_000)
    even_fibs = [f for f in fibonaccis if f%2==0]
    print(fibonaccis, even_fibs, sum(even_fibs))
    pass    

# #http://radiusofcircle.blogspot.com

# #imported time module for calculating execution time
# import time

# #Program Start time
# start_time = time.time()

# #All variables ending with
# # 1 - Example program given in question
# # 2 - Solution we will have to find out

# #program for Example given in Question

# #Variables required for program
# first_number1 = 0
# second_number1 = 1
# fibonacci1 = 0
# even_sum1 = 0

# #While loop to run till the value of fibonacci < 101
# while fibonacci1 <= 100:
# 	fibonacci1 = first_number1 + second_number1
# 	first_number1 = second_number1
# 	second_number1 = fibonacci1
# 	if fibonacci1 % 2 == 0:
# 		even_sum1 += fibonacci1

# #Print(ng the output of example)
# print('Sum of Even Fibonacci Numbers')
# print('Which are less than 100 is')
# print('{}\n'.format(even_sum1))

# #Variables required for question
# first_number2 = 0
# second_number2 = 1
# fibonacci2 = 0
# even_sum2 = 0

# #While loop to run till fibonacci <= 4 million
# while fibonacci2 <= 4000000:
# 	fibonacci2 = first_number2 + second_number2
# 	first_number2 = second_number2
# 	second_number2 = fibonacci2
# 	if fibonacci2 % 2 == 0:
# 		even_sum2 += fibonacci2

# #Print(ng the output of the solution)
# print('Sum of Even Fibonacci Numbers')
# print('Which are less than 4 million is')
# print('{}\n'.format(even_sum2))

# #Time at the end of the program
# end_time = time.time()

# #Total Time taken
# total_time = end_time - start_time

# #Print(ng the total time taken)
# print('Total time taken is {}'.format(total_time))