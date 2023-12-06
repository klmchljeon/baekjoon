t = int(input())
for case in range(t):
    h,w = map(int,input().split())
    d = [input() for _ in range(h)]

    for i in d:
        print(i[::-1])