n = int(input())
res = 0
for _ in range(n):
    q = input()
    q = q.replace('0','9')
    q = q.replace('6','9')
    res += min(100, int(q))

div,mod = divmod(res,n)
if mod*2 >= n:
    div += 1

print(div)