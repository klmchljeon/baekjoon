n = int(input())
d = [0] + list(map(int,input().split()))

cnt = 0
for i in range(1,n+1):
    cnt += d[i]!=i
    
print(cnt)