n = int(input())
if n==2:
    print(2,4)
    exit()

d = list(range(2,2*n,2))

t = 3
s = sum(d)
while True:
    if (s+t)%t == 0:
        d.append(t)
        break

    t += 2

print(*d)