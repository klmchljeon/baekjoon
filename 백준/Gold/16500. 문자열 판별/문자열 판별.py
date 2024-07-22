st = input()
n = int(input())
lst = [input() for _ in range(n)]

check = [0]*(len(st))
for s in lst:
    m = len(s)
    if st[:m] == s and m-1 < len(st):
        check[m-1] = 1

for i in range(len(st)-1):
    if not check[i]: continue

    for s in lst:
        m = len(s)
        if st[i+1:i+m+1] == s and i + m < len(st):
            check[i + m] = 1

print(check[-1])