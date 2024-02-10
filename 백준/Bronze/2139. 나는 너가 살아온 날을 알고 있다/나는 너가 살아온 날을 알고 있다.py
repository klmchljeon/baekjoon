import datetime

while True:
    d,m,y = map(int,input().split())
    if not (d or m or y): break

    a = datetime.date(y,m,d)
    b = datetime.date(y,1,1)
    print((a-b).days + 1)