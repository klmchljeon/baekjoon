n = int(input())
lst = list(map(int,input().split()))
for i in range(n-1):
    if lst[i] == lst[i+1]:
        print(0)
        break

else:
    print(1)