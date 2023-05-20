conv = lambda x:sum(map(int,str(x)))

n = int(input())

cnt = n
for i in range(1,n+1):
    cnt -= bool(i%conv(i))

print(cnt)