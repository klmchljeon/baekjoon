n = int(input())
d = list(map(int,input().split()))

c = int(input())
cnt = 0
for i in d:
    cnt += i//c + bool(i%c)

print(cnt*c)