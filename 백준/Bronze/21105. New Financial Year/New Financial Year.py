n = int(input())
for case in range(n):
    p,c = map(float,input().split())
    print(100*p / (c+100))