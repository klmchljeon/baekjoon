n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnt = 0
for i in range(n):
    cnt += (a[i]>b[i])*(a[i]-b[i])
    
print(cnt)