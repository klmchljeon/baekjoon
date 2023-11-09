d = list(map(int,input().split()))
m = d.pop()

print(max(0,4*m - sum(d)))