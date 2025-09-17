n = int(input())
st = input()
p = 0
q = 0
for i in st:
    if i == 'N':
        p += 1

    if i == 'E':
        q += 1

    if i == 'S':
        p -= 1

    if i == 'W':
        q -= 1

print(abs(p) + abs(q))