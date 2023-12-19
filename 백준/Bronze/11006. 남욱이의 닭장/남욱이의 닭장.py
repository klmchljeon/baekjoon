t = int(input())
for case in range(t):
    a,b = map(int,input().split())
    c = b*2 - a
    print(c,b-c)