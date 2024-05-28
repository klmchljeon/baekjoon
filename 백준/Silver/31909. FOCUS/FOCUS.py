import sys
input = sys.stdin.readline

lst = [None]*256
for i in range(7):
    for j in range(i+1,8):
        x = 2**i + 2**j

        lst[x] = (i,j)

n = int(input())
d = list(map(int,input().split()))
k = int(input())

key = list(range(8))
for x in d:
    if lst[x] == None: continue

    i,j = lst[x]
    key[i],key[j] = key[j],key[i]

print(key[k])