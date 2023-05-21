n,s = map(int,input().split())
d = list(map(int,input().split()))

idx = 0
while True:
    if d[idx%n] < s+idx:
        break

    idx += 1

print(idx%n+1)