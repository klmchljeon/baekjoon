d = [list(map(int,input().split())) for _ in range(3)]
h = int(input())

t = -1
while h > 0:
    t += 1

    for c,da in d:
        if t%c == 0:
            h -= da

print(t)