t = int(input())
for case in range(t):
    n = int(input())
    d = list(map(int,input().split()))
    print(2*(max(d)-min(d)))