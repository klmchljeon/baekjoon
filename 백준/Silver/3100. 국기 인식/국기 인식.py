alpha = [chr(i+ord('A')) for i in range(26)]

d = [input() for _ in range(6)]

res = 0
for f in alpha:
    for s in alpha:
        for t in alpha:
            if f==s or s==t: continue

            cnt = 0
            for i in range(0,2):
                for j in range(9):
                    cnt += d[i][j] == f

            for i in range(2,4):
                for j in range(9):
                    cnt += d[i][j] == s

            for i in range(4,6):
                for j in range(9):
                    cnt += d[i][j] == t

            res = max(res,cnt)

            cnt = 0
            for i in range(6):
                for j in range(0,3):
                    cnt += d[i][j] == f

            for i in range(6):
                for j in range(3,6):
                    cnt += d[i][j] == s

            for i in range(6):
                for j in range(6,9):
                    cnt += d[i][j] == t

            res = max(res,cnt)

print(54-res)