def check(s,e):
    if s==e: 
        return True

    l,r = s,e
    while l!=r:
        if not lst[l]^lst[r]:
            return False
        
        l += 1
        r -= 1

    mid = (s+e)//2
    return check(s,mid-1) and check(mid+1,e)

t = int(input())
for case in range(t):
    lst = list(map(int,input()))
    print('YES' if check(0,len(lst)-1) else 'NO')