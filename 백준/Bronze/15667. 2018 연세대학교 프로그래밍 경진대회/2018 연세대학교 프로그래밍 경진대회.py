n = int(input())
for i in range(1,101):
    if i**2 + i + 1 == n:
        print(i)
        break