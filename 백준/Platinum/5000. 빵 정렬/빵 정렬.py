def update(idx,val,s,e,node):
    if s==e:
        tree[node] = val
        return 

    m = (s+e)//2
    if idx <= m:
        update(idx,val,s,m,node*2)
    else:
        update(idx,val,m+1,e,node*2+1)

    tree[node] = tree[node*2] + tree[node*2+1]
    return

def cal(l,r,s,e,node):
    if e<l or r<s:
        return 0
    
    if l<=s and e<=r:
        return tree[node]
    
    m = (s+e)//2
    left = cal(l,r,s,m,node*2)
    right = cal(l,r,m+1,e,node*2+1)
    
    return left+right

n = int(input())
a = list(map(int,input().split()))
d = [0]*(n+1)
for i in range(n):
    d[a[i]] = i

b = list(map(int,input().split()))
lst = [(d[b[i]],i) for i in range(n)]
lst.sort()

tree = [0]*(n*4)

cnt = 0
for _,i in lst:
    tmp = cal(i+1,n,1,n,1)
    update(i+1,1,1,n,1)
    cnt += tmp

print("Possible" if cnt%2==0 else "Impossible")