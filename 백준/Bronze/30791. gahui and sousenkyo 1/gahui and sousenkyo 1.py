a,*d = map(int,input().split())
cnt = 0
for i in d:
    cnt += (a-1000)<=i
    
print(cnt)