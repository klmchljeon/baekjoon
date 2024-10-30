import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    st = input().rstrip()
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            print('No')
            break

    else:
        print('Yes')