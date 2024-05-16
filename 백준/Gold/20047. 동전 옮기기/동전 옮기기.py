n = int(input())
s = list(input()) + ['']*2
t = list(input())
u,v = map(int,input().split())

b = s.pop(v)
a = s.pop(u)

for k in range(n-1):
    j = 0
    while j < k:
        if s[j] != t[j]:
            break

        j += 1

    if j != k or a != t[j]:
        continue

    i = j
    j += 1
    flag = True
    while j < n:
        if s[i] == t[j]:
            i += 1
            j += 1
            continue

        if flag and b == t[j]:
            flag = False
            j += 1
        else:
            break

    else:
        print('YES')
        break

else:
    print('NO')