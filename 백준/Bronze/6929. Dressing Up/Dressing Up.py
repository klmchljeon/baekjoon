h = int(input())
for i in range(1,h+1,2):
    print('*'*i + ' '*(h-i)*2 + '*'*i)

for i in range(1,h-1,2)[::-1]:
    print('*'*i + ' '*(h-i)*2 + '*'*i)