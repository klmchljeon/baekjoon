n,m = map(int,input().split())
lst = [0] + list(map(int,input().split()))
for _ in range(m):
    l,h = map(int,input().split())
    if lst[h] != max(lst):
        lst[l] -= 1

print(*lst[1:])