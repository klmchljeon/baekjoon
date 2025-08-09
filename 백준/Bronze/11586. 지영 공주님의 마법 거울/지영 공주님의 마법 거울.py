n = int(input())
lst = [input() for _ in range(n)]
k = int(input())
if k == 2:
    for i in range(n):
        lst[i] = lst[i][::-1]

elif k == 3:
    lst = lst[::-1]

for i in lst:
    print(i)