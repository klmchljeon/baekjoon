#다면체
t = int(input())
for case in range(t):
    v,e = map(int,input().split())
    print(e-v+2)