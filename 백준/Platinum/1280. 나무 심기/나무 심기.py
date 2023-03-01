#나무 심기
import sys
input = sys.stdin.readline
t = 200000
mod = 1000000007

def cal(l,r,s,e,node=0):
    if l<=s and e<=r:
        return tree[node]

    if e<l or r<s:
        return [0,0]

    m = (s+e)//2
    le = cal(l,r,s,m,node*2+1)
    ri = cal(l,r,m+1,e,node*2+2)

    return [(le[0]+ri[0])%mod, le[1]+ri[1]]

def update(val,s,e,node=0):
    if s==e and s==val:
        tree[node][0] += val
        tree[node][1] += 1
        return 

    if val<s or e<val: 
        return 

    m = (s+e)//2
    update(val,s,m,node*2+1)
    update(val,m+1,e,node*2+2)
    le = tree[node*2+1]
    ri = tree[node*2+2]

    tree[node] = [(le[0]+ri[0])%mod, le[1]+ri[1]]
    return 

n = int(input())
tree = [[0,0] for _ in range(t*4)]

fir = int(input())
update(fir,0,t-1)

res = 1
for i in range(n-1):
    a = int(input())
    update(a,0,t-1)
    s1,lens1 = cal(0,a,0,t-1)
    s2,lens2 = cal(a,t-1,0,t-1)
    
    tmp = lens1*a-s1 + s2-lens2*a
    res = res*tmp%mod

print(res)