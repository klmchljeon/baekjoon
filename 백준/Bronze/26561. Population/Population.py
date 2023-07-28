n = int(input())
for case in range(n):
    p,t = map(int,input().split())
    print(p - t//7 + t//4)