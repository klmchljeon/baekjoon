n = int(input())
cnt = 0
for b in range(1,n-2):
    for c in range(b+2,n-b):
        a = n - (b+c)
        cnt += a%2==0 and a>0

print(cnt)