alpha = [chr(i + ord('a')) for i in range(26)]
dic = dict(zip(alpha,range(26)))

st = input()

d = [0]*26
for i in st:
    d[dic[i]] += 1

n = len(st)
m = (n+1)//2
for i in d:
    if i > m:
        print(-1)
        exit()

res = [None]*n
for i in range(m):
    for j in range(26):
        if d[j] >= 1:
            d[j] -= 1
            res[i] = alpha[j]
            break

for i in range(m,n):
    for j in range(26):
        if d[j] >= 1 and res[n-i-1] != alpha[j]:
            d[j] -= 1
            res[i] = alpha[j]
            break

print(''.join(res))