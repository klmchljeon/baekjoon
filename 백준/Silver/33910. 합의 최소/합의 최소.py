n = int(input())
lst = list(map(int,input().split()))

res = 0
p = lst[-1]
for i in lst[::-1]:
    p = min(p,i)
    res += p

print(res)