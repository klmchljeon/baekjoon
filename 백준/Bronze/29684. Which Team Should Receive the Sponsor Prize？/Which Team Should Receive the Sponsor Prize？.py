f = lambda x:abs(x[0]-2023)

while True:
    n = int(input())
    if n == 0: break

    d = list(map(int,input().split()))

    lst = list(zip(d,range(1,n+1)))
    lst.sort(key = f)

    print(lst[0][1])