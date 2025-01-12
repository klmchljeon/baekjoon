h,w = map(int,input().split())
lst = [list(map(int,input())) for _ in range(h)]
cnt = 0
for i in range(h):
    for j in range(w):
        cnt += lst[i][j]

print(min(cnt,h*w-cnt))