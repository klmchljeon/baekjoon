#과제는 끝나지 않아!
import sys
input = sys.stdin.readline

n = int(input())
d = []
score = 0
for i in range(n):
    q,*at = map(int,input().split())
    if q == 1:
        d.append(at)

    if not d: continue

    d[-1][1] -= 1
    if d[-1][1] == 0:
        score += d[-1][0]
        d.pop()

print(score)