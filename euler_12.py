

def get_divisors(num):
    divisors = [1,num]
    for i in range(2,int(num**(1/2)+1)):
        if i not in divisors:
            if num % i == 0:
                divisors.append(i)
                if num//i not in divisors:
                    divisors.append(num//i)
    # if 2 in divisors:
    #     divisors.append(num/2)

    return sorted(divisors)

def divide(num):
    divisors = []
    i = 2
    while num > 0:
        if num % i:
            divisors.append(i)

    pass

if __name__ == "__main__":
    

    num = 1
    i = 1
    divisors = []
    exp = 1
    while len(divisors) < 500:
        i += 1
        num += i
        divisors = get_divisors(num)
        # if num > 10**exp:
        #     print(num)
        #     exp += 1
    print(num,":",divisors)