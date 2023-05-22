n,k = map(int,input().split())
d = list(map(int,input().split()))
cnt = 0
for i in d:
    cnt += i//2 + i%2

print('YES' if n<=cnt else 'NO')