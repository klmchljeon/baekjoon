#스위치 켜고 끄기
n = int(input())
d = [-1] + list(map(int,input().split()))

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    if a==1:
        for i in range(b,n+1,b):
            d[i] ^= 1

    else:
        d[b] ^= 1

        l,r = b-1,b+1
        while 1<=l and r<=n:
            if d[l] == d[r]:
                d[l] ^= 1
                d[r] ^= 1
            else:
                break

            l -= 1
            r += 1

for i in range(1,n,20):
    print(*d[i:i+20])