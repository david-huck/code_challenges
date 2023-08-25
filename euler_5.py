
def evenly_divisible(num, divisors):
    for div in divisors:
        if num%div!=0:
            return False
    return True

if __name__=="__main__":
    
    for i in range(int(2*3*5*7*11*13*17*19), int(1e10), 19):
        if evenly_divisible(i,range(1,21)):
            print(i) # 232792560
            break
    # print(evenly_divisible(2520, range(1,11)))
        
    pass