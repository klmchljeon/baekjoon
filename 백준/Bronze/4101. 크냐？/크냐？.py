import sys
input = sys.stdin.readline
while True:
    a,b = map(int,input().split())
    if a==0:
        break;
    if a>b:
        sys.stdout.write("Yes\n")
    else:
        sys.stdout.write("No\n")