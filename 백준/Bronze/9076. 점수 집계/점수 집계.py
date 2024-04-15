n = int(input())
for case in range(n):
    lst = list(map(int,input().split()))
    lst.sort()

    lst.pop()
    lst.pop(0)

    if lst[-1] - lst[0] >= 4:
        print("KIN")
    else:
        print(sum(lst))