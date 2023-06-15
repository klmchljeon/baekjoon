#두 배열의 합
t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

prefix = [0]
s = 0
for i in range(n):
    s += a[i]
    prefix.append(s)

dica = dict()
for i in range(n+1):
    for j in range(i+1,n+1):
        tmp = prefix[j]-prefix[i]
        if not tmp in dica:
            dica[tmp] = 0

        dica[tmp] += 1

prefix = [0]
s = 0
for i in range(m):
    s += b[i]
    prefix.append(s)

dicb = dict()
for i in range(m+1):
    for j in range(i+1,m+1):
        tmp = prefix[j]-prefix[i]
        if not tmp in dicb:
            dicb[tmp] = 0

        dicb[tmp] += 1

cnt = 0
for v in dica:
    if t-v in dicb:
        cnt += dica[v]*dicb[t-v]

print(cnt)