lst1 = [
    [200,210,220],
    [210,220,225],
    [220,225,230],
    [225,230,235],
    [230,235,245],
    [235,245,250]
]
lst2 = [
    [260,265,270],
    [265,270,275],
    [270,275,280],
    [275,280,285],
    [280,285,290],
    [285,290,295],
    [290,295,300]
]

n = int(input())
for lst in lst1,lst2:
    res = []
    for a,b,c in lst:
        if n < a:
            res.append(0)
        elif n < b:
            res.append(500)
        elif n < c:
            res.append(300)
        else:
            res.append(100)

    print(*res)
        