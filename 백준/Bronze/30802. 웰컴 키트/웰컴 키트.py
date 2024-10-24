n = int(input())
lst = list(map(int,input().split()))
t,p = map(int,input().split())

cnt = 0
for i in lst:
    cnt += i//t + bool(i%t)

print(cnt)
print(*divmod(n,p))