t = int(input())
for case in range(t):
    n,*lst = map(int,input().split())
    lst.sort()

    max_ = lst[n-1]
    min_ = lst[0]
    gap = 0
    for i in range(n-1):
        gap = max(gap,lst[i+1]-lst[i])

    print(f'Class {case+1}')
    print(f'Max {max_}, Min {min_}, Largest gap {gap}')