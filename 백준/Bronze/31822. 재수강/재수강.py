st = input()
n = int(input())

cnt = 0
for _ in range(n):
    tmp = input()
    cnt += st[:5] == tmp[:5]

print(cnt)