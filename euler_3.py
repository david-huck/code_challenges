from math import sqrt

def is_prime(num):
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return False
    return True

if __name__=="__main__":
    p_facs = []
    our_num = 600851475143

    i=2
    remainder = None
    while len(p_facs) == 0:
        if is_prime(i) and our_num%i==0:
            remainder = our_num / i
            p_facs.append(i)
        i += 1

    while remainder > 1:
        c_p_fac_len = len(p_facs)
        for p in p_facs:
            while remainder % p == 0:
                remainder /= p
                continue
        # find next p_fac
        i = p_facs[-1]
        while len(p_facs) == c_p_fac_len and remainder > 1:
            if is_prime(i) and remainder%i==0 and i not in p_facs:
                p_facs.append(i)
            if i > remainder:
               raise ValueError("something went wrong.")
            i += 1
        
    # for i in range(p_facs[0]+1,int(our_num/p_facs[0])+1):
    #     if is_prime(i) and our_num%i==0:
    #         p_facs.append(i)
    #     if i%100000==0:
    #         print("@",i)
    print(p_facs)