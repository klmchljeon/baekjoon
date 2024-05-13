d = [int(input()) for _ in range(4)]
f1 = d[0] in (8,9)
f2 = d[1] == d[2]
f3 = d[3] in (8,9)

res = f1 and f2 and f3
print('ignore' if res else 'answer')