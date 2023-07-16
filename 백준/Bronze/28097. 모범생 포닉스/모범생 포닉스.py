n = int(input())
d = list(map(int,input().split()))

res = sum(d)+8*(n-1)
print(*divmod(res,24))