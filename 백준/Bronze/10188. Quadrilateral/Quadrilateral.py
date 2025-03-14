t = int(input())
for case in range(t):
    x,y = map(int,input().split())
    for i in range(y):
        print('X'*x)

    if case != t-1:
        print()