d = [35034,23090,19055,12530,18090]
n = int(input())
for _ in range(n):
    lst = list(map(int,input().split()))
    res = 0
    for i in range(5):
        res += lst[i]*d[i]

    print(f'${res//100}.{res%100:02d}')