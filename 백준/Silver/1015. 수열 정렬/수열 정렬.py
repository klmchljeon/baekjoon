#수열 정렬
n = int(input())
d = list(map(int,input().split()))

lst = sorted(zip(d,range(n)))

res = [0]*n
for i in range(n):
    res[lst[i][1]] = i

print(*res)