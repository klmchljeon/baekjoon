import sys
input = sys.stdin.readline

def find(num):
    s,e = -1,len(d)
    while s+1<e:
        mid = (s+e)//2

        if d[mid] > num:
            e = mid
        
        else:
            s = mid

    return e


n,h = map(int,input().split())
lst = []
for i in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))
lst.append((h+1,h+1))

q = int(input())
query = []
for i in range(q):
    t = int(input())
    query.append(t)

lst.sort(key = lambda x:(x[0],-x[1]))
head,tail = lst[0]
d = [head]
for s,e in lst:
    if tail < s:
        d.append(s-tail)
        head,tail = s,e

    else:
        tail = max(tail,e)

d.sort()
prefix = [0]
s = 0
for i in d:
    s += i
    prefix.append(s)

m = len(d)
for num in query:
    idx = find(num)

    p = prefix[m] - prefix[idx]
    q = (m-idx)*num

    print(p-q)