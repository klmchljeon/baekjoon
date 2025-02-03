n = int(input())
lst = list(map(int,input().split()))

cur = 0
s = 0
for i in lst:
    if i == 1:
        cur += 1
    else:
        cur -= 1

    s += cur

print(s)