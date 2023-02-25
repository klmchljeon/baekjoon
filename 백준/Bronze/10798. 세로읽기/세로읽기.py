#세로읽기
st = [list(input())[::-1] for _ in range(5)]

res = ''
for _ in range(15):
    for i in range(5):
        if not st[i]: continue

        res += st[i].pop()

print(res)