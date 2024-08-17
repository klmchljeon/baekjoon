n = int(input())
lst = input().split()
st = input()

cnt = 0
for i in lst:
    cnt += st==i

print(cnt)