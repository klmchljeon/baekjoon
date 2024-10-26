#버블 소트
import sys
input = sys.stdin.readline

def update(idx,val,s,e,node=1):
    if s==e:
        tree[node] += val
        return 

    m = (s+e)//2
    if idx <= m:
        update(idx,val,s,m,node*2)
    else:
        update(idx,val,m+1,e,node*2+1)

    tree[node] += val
    return 

def cal(l,r,s,e,node=1):
    if e<l or r<s:
        return 0

    if l<=s and e<=r:
        return tree[node]

    m = (s+e)//2
    left = cal(l,r,s,m,node*2)
    right = cal(l,r,m+1,e,node*2+1)
    return left + right

n = int(input())
lst = [0] + [int(input()) for _ in range(n)]

d = []
for i in range(1,n+1):
    d.append((i,lst[i]))

t = lambda x:x[1]
d.sort(key = t)

tree = [0]*(n*4)

res = [i for i in range(n+1)]
for i in range(n):
    res[d[i][0]] -= cal(1,d[i][0],1,n)
    update(d[i][0],1,1,n)

print(*res[1::],sep='\n')