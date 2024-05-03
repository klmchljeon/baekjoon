n = int(input())
d = list(map(int,input().split()))

res = 0
prev = None
for i in d:
    if i%2 != prev:
        res += 1
        prev = i%2

print(res)