n = int(input())
lst = [int(input()) for _ in range(n)]

flag = True
for i in range(1,lst[-1]+1):
    if not i in lst:
        flag = False
        print(i)

if flag:
    print("good job")