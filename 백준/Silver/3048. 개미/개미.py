n,m = map(int,input().split())
a = input()
b = input()
t = int(input())

lst = ['']*100
i = 2*n - 1
for c in b:
    lst[i] = c
    i += 2

i = t*2
for c in a[::-1]:
    lst[i] = c
    i += 2

print(''.join(lst))