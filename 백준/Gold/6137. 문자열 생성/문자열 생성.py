#문자열 생성
import sys
sys.setrecursionlimit(2500)

def cal(s,e,st=''):
    if s > e: 
        return st
    
    if d[s] < d[e]:
        return cal(s+1,e, st + d[s])
    
    elif d[s] < d[e]:
        return cal(s,e-1, st + d[e])
    
    else:
        if find(s,e):
            return cal(s+1,e, st + d[s])
        else:
            return cal(s,e-1, st + d[e])
        
def find(l,r):
    if l >= r:
        return True
    
    if d[l] == d[r]:
        return find(l+1,r-1)
    
    else:
        return d[l] <= d[r]

n = int(input())
d = [input() for _ in range(n)]

res = cal(0,n-1)
for i in range(0,n,80):
    print(res[i:i+80])