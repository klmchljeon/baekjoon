#중복 없는 수
import sys
input = sys.stdin.read

def dfs(m):
    if len(s) == m:
        lst.append(conv(s))
        return 
    
    for i in num:
        if not i in s:
            s.append(i)
            dfs(m)
            s.pop()
    
def find(i):
    lo,hi = -1,n
    while lo+1 < hi:
        mid = (lo+hi)//2

        if lst[mid] > i:
            hi = mid
        else:
            lo = mid

    return lst[hi]

conv = lambda x:int(''.join(x))
num = '123456789'
inf = 987654321

lst = []
s = []
for i in range(1,10):
    dfs(i)

lst.sort()
n = len(lst)

d = list(map(int,input().split()))

for i in d:
    res = find(i) if i < inf else 0
    print(res)