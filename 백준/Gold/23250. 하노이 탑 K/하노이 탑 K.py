#하노이 탑 K
def find(s,e,depth,tar):
    if depth == 1:
        return (s,e)

    m = 6-(s+e)
    idx = 2**(depth-1)
    if tar == idx:
        return (s,e)

    elif tar < idx:
        return find(s,m,depth-1,tar)

    else:
        return find(m,e,depth-1,tar-idx)

n,k = map(int,input().split())
res = find(1,3,n,k)
print(*res)