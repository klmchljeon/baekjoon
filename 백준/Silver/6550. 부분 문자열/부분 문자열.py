#부분 문자열
import sys
input = sys.stdin.readline

while True:
    try:
        s,t = map(list,input().split())
    except:
        break

    while s and t:
        if s[-1] == t[-1]:
            s.pop()
            t.pop()

        else:
            t.pop()

    if not s:
        print('Yes')
    else:
        print('No')