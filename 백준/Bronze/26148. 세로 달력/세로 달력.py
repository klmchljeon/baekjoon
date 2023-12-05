a = int(input())
_ = int(input())

l=0
if a%4==0:
    l=1
    if a%100==0:
        l=0
        if a%400==0:
            l=1

print(29+l)