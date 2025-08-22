n = int(input())
p = 0
while n%2 == 0:
    n = n//2
    p += 1

print(n,p)