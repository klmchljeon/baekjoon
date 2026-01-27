n = int(input())
a,b = input().split('*')
for _ in range(n):
    st = input()
    if len(a) + len(b) > len(st):
        print('NE')
        continue

    if a == st[:len(a)] and b == st[-len(b):]:
        print('DA')
    else:
        print('NE')