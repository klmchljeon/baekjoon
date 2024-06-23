from math import log2

n = int(input())
lst = list(map(int,input().split()))

for i in range(n):
    lst[i] = log2(lst[i])

res = 0
for i in range(1,n):
    while lst[i-1] > lst[i]:
        lst[i] += 1
        res += 1

print(res)