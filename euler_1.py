def get_multiples_of(nums, end):
    mults = []
    for i in range(end):
        for div in nums:
            if i%div==0 and i not in mults:
                mults.append(i)
            
    return mults

if __name__ == "__main__":
    multiples = get_multiples_of([3,5], 100)
    print(multiples)
    print(sum(multiples))