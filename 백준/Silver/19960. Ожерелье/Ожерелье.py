n = int(input())

if n < 6:
    print(-1)

else:
    print(*([0,0,1,0] + [1]*(n-4)))