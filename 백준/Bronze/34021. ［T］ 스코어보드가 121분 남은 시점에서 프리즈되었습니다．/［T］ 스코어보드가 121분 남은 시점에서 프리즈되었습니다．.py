t = int(input())
for case in range(t):
    n,m,l = map(int,input().split())
    lst = list(map(int,input().split()))
    p = l
    for i in lst:
        if i == -1:
            continue

        p = max(p,m-i)

    if p != 1:
        print(f"The scoreboard has been frozen with {p} minutes remaining.")
    else:
        print("The scoreboard has been frozen with 1 minute remaining.")