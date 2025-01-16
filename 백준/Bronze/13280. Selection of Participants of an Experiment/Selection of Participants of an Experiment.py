while True:
    n = int(input())
    if not n: break

    lst = list(map(int,input().split()))
    lst.sort()

    tmp = [lst[i+1]-lst[i] for i in range(n-1)]
    print(min(tmp))