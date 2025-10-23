n = int(input())
m = int(input())
for _ in range(m):
    q = input()
    num = int(input())
    if q == '+':
        n += num
    else:
        n -= num

print(n)