n = int(input())
st = input()
p = 'eagle'
res = 5
for i in range(len(st)-4):
    cnt = 0
    for j in range(5):
        cnt += st[i+j]==p[j]

    res = min(res,5-cnt)

print(res)