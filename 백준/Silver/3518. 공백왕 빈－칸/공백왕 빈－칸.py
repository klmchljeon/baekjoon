import sys
input = sys.stdin.read

p = input().split('\n')
lst = [i.split() for i in p]
n = len(lst)

m = len(max(lst,key = len))
tmp = []
for j in range(m):
    x = 0
    for i in range(n):
        if j >= len(lst[i]): continue
        x = max(x,len(lst[i][j]))

    tmp.append(x)

for i in range(n):
    for j in range(len(lst[i])-1):
        lst[i][j] += ' '*(tmp[j]-len(lst[i][j]))

    print(*lst[i])