n = int(input())
lst = []
for i in range(2):
    tmp = list(map(int,input().split()))
    lst.append(tmp)

f1 = False
for j in range(n):
    for i in range(2):
        f1 |= lst[i][j]==0

if not f1:
    print(2)
    exit()

for j in range(n-1):
    p = False
    for i in range(2):
        p |= lst[i][j]==lst[i][j+1] and lst[i][j]

    if not p:
        print(0)
        break

else:
    print(1)