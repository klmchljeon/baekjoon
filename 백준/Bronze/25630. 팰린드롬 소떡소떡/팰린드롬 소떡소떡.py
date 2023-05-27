n = int(input())
st = input()

cnt = 0
for i in range(n):
    cnt += st[i] != st[n-i-1]

print(cnt//2)