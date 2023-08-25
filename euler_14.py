# largest collatz sequence
import plotly.express as px
import pandas as pd

import sys
# sys.setrecursionlimit(10**6)

def collatz_rec(num):
    if num == 1:
        return [num]
    elif num % 2 == 1:
        return [num] + collatz_rec(3*num + 1)
    else:
        return [num] + collatz_rec(num/2)
    
if __name__=="__main__":
    sequence_lengths = []
    # df = pd.DataFrame()
    longest_sequence_start = 1
    for i in range(1,1_000_000):
        current_sequence = collatz_rec(i)
        # sequences.append(current_sequence)
        # df.at[i,"len"] = len(current_sequence)
        sequence_lengths.append(len(current_sequence))
        if len(current_sequence) > longest_sequence_start:
            longest_sequence_start = i
    
    # df = pd.DataFrame(sequence_lengths, index=range(1,1_000_000))
    # df.to_csv("collatz_sequence_length.csv")
    print(longest_sequence_start)
