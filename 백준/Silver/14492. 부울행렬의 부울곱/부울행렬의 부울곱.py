#부울행렬의 부울곱
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

res = []
for i in range(n):
    cal = []
    for j in range(n):
        row = 0
        for k in range(n):
            row |= a[i][k]&b[k][j]

        cal.append(row)

    res.append(cal)

f = lambda x:x.count(True)
print(sum(map(f,res)))