n = int(input())
d = [int(input()) for _ in range(n)]
if d[0]+d[2] == d[1]*2:
    print(d[n-1] + (d[1]-d[0]))
else:
    print(d[n-1] * (d[1]//d[0]))