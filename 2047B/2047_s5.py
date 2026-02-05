from collections import Counter
from math import factorial

def permutations_count(s):
    freq = Counter(s)
    res = factorial(len(s))
    for c in freq.values():
        res //= factorial(c)
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    best = None
    best_val = float('inf')

    for i in range(n):
        for j in range(n):
            temp = list(s)
            temp[i] = temp[j]   # exactly one operation
            temp = "".join(temp)

            val = permutations_count(temp)
            if val < best_val:
                best_val = val
                best = temp

    print(best)