#내 학점을 구해줘
t = int(input())
for case in range(t):
    n = int(input())
    s = 0
    cnt = 0
    for _ in range(n):
        a,b = input().split()
        a = int(a); b = float(b)
        s += a*b
        cnt += a

    print(cnt,s/cnt)