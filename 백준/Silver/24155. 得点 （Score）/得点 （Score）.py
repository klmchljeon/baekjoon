import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    s = int(input())
    lst.append((s,i))

lst.sort(reverse=True)

res = [-1]*n
prev = None
rank = None
for r in range(n):
    s,i = lst[r]
    if s == prev:
        res[i] = rank

    else:
        res[i] = r+1
        prev = s
        rank = r+1

print(*res,sep='\n')