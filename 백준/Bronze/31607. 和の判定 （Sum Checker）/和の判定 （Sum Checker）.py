d = [int(input()) for _ in range(3)]
d.sort()

res = d[0]+d[1]==d[2]
print(int(res))