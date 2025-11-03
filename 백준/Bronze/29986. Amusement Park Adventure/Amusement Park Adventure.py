n,h = map(int,input().split())
lst = list(map(int,input().split()))
cnt = 0
for i in lst:
    cnt += i <= h
    
print(cnt)