from collections import deque

def cal(p):
    res = 0
    for i in range(1,n):
        res += abs(p[i]-p[i-1])

    return res

n = int(input())
lst = list(map(int,input().split()))
lst.sort()

arr = lst[:]

cen = n//2

a,b = lst.pop(cen),lst.pop(cen-1)
res = []

d = deque(lst)
flag = 0
while d:
    if flag:
        res.append(d.popleft())

    else:
        res.append(d.pop())

    flag ^= 1

res1 = [b] + res + [a]

lst = arr[:]
a,b = lst.pop(cen+1),lst.pop(cen)
res = []

d = deque(lst)
flag = 1
while d:
    if flag:
        res.append(d.popleft())

    else:
        res.append(d.pop())

    flag ^= 1

res2 = [a] + res + [b]

print(max(cal(res1),cal(res2)))