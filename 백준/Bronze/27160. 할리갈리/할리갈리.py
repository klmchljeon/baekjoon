import sys
input = sys.stdin.readline

n = int(input())

dic = dict()

for _ in range(n):
    s,x = input().split()
    x = int(x)

    if not s in dic:
        dic[s] = x
    else:
        dic[s] += x

flag = True
for i in dic:
    if dic[i] == 5:
        flag = False

if flag:
    print('NO')
else:
    print('YES')