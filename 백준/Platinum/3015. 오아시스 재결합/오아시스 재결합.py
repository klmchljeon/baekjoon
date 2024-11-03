#오아시스 재결합
import sys
input = sys.stdin.readline

n = int(input())
d = [(int(input()),1)]
count = 0

for i in range(1,n):
    a = int(input())

    c = 1
    while d:
        if d[-1][0] < a:
            _,x = d.pop()
            count += x

        elif d[-1][0] == a:
            c = d[-1][1] + 1
            _,x = d.pop()
            count += x

        else:
            break
            
    if d:
        count += 1
    d.append((a,c))
    
print(count)