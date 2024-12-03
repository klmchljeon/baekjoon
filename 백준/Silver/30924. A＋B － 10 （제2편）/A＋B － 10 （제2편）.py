import sys
import random
input = sys.stdin.readline

lsta = list(range(1,10001))
random.shuffle(lsta)

cnt = 0
a = None
while cnt < 9999:
    tmp = lsta.pop()
    print(f'? A {tmp}')
    sys.stdout.flush()

    cnt += 1
    res = int(input())
    if res:
        a = tmp
        break

if a == None:
    a = lsta.pop()

b = None

lstb = list(range(1,10001))
random.shuffle(lstb)
while cnt < 19997:
    tmp = lstb.pop()
    print(f'? B {tmp}')
    sys.stdout.flush()
    
    cnt += 1
    res = int(input())
    if res:
        b = tmp
        break

if b == None:
    b = random.choice(lstb)

print(f'! {a+b}')