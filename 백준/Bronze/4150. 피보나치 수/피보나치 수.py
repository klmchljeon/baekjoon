d = [0,1]
n = int(input())
for i in range(n-1):
    d.append(d[-1]+d[-2])

print(d[n])