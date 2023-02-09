import sys
input = sys.stdin.readline

def propagate(s,e,node):
    val = lazy[node]
    if val:
        if s!=e:
            lazy[node*2] += val
            lazy[node*2+1] += val
    
        else:
            d[s] += val
        
        lazy[node] = 0

    return 

def update(l,r,val,s,e,node=1):
    propagate(s,e,node)

    if e<l or r<s:
        return

    if l<=s and e<=r:
        lazy[node] += val
        propagate(s,e,node)
        return 

    if l<=e or s<=r:
        m = (s+e)//2 
        update(l,r,val,s,m,node*2)
        update(l,r,val,m+1,e,node*2+1)
        return 
    
def cal(idx,s,e,node=1):
    propagate(s,e,node)

    if s==e:
        return d[s]
    
    m = (s+e)//2
    if idx <= m:
        return cal(idx,s,m,node*2)
    else:
        return cal(idx,m+1,e,node*2+1)

n = int(input())
d = [0]+list(map(int,input().split()))
lazy = [0]*(n*4)

m = int(input())
for query in range(m):
    q,*order = map(int,input().split())
    if q==1:
        update(*order,1,n)

    else:
        print(cal(*order,1,n))