p = sum(input()=='W' for _ in range(6))
if p >= 5:
    print(1)
elif p >= 3:
    print(2)
elif p >= 1:
    print(3)
else:
    print(-1)