t = int(input())
for case in range(t):
    st = input()
    cnt = 0
    for i in range(len(st)-2):
        cnt += st[i:i+3] == "WOW"

    print(cnt)