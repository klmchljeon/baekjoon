#N결수
n,k = map(int,input().split())
dig = 1
m = 10

res = 1
for i in range(2,n+1):
    if i == m:
        m *= 10
        dig += 1

    res = (res*(m%k) + i%k)%k

print(res%k)