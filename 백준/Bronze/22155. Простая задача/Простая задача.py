n = int(input())
for case in range(n):
    a,b = map(int,input().split())
    f1 = (a+b) <= 3
    f2 = a < 3 and b < 3
    print('Yes' if f1 and f2 else 'No')