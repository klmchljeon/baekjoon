#바둑돌 게임
win = []
i = 1
while True:
    win.append([i*(i+1)//2,(i+1)*(i+2)//2])
    if win[-1][0] > 100000:
        break
    i += 2

n = int(input())
for i in range(len(win)):
    if win[i][0] <= n < win[i][1]:
        print(0)
        break

    if win[i][1] <= n < win[i+1][0]:
        print(win[i+1][0]-n)
        break