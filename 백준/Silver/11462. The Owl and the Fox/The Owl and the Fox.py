import sys
input = sys.stdin.readline

while True:
    st = input().rstrip()
    if st == 'END':
        break

    p = sum(map(int,st))
    n = int(st)
    for i in range(n)[::-1]:
        if sum(map(int,str(i))) == p-1:
            print(i)
            break