t = int(input())
for case in range(t):
    n = int(input())
    for i in range(n+1)[::-1]:
        if i + i**2 <= n:
            print(i)
            break