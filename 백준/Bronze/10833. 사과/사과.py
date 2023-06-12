#사과
n = int(input())
res = 0
for i in range(n):
    a,b = map(int,input().split())
    res += b%a

print(res)