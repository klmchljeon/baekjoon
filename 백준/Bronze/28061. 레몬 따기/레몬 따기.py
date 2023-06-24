#레몬 따기
n = int(input())
d = list(map(int,input().split()))

res = 0
for i in d:
    res = max(res,i-n)
    n -= 1

print(res)