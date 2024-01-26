t = int(input())
for case in range(t):
    input()
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort(reverse = True)
    b.sort(reverse = True)

    while a and b:
        if a[-1] < b[-1]:
            a.pop()
        else:
            b.pop()

    if a:
        print('S')
    else:
        print('B')