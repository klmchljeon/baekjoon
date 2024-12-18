n = int(input())
cnt = 0
for _ in range(n):
    d = int(input())
    cnt += d%2
    
print(cnt)