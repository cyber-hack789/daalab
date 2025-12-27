 
#2.Write a program to perform Travelling Sales man Problem. 

import itertools

d = [
    [0,16,11,6],
    [8,0,13,16],
    [4,7,0,9],
    [5,12,2,0]
]

n = len(d)
mc = 9999
best = None

for p in itertools.permutations(range(n)):
    c = sum(d[p[i]][p[i+1]] for i in range(n-1)) + d[p[-1]][p[0]]

    if c < mc:        # 🔑 important condition
        mc = c
        best = p

print("Minimum Cost:", mc)
print("Best Path:", list(best) + [best[0]])
