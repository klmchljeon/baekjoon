a = ['Algorithm','DataAnalysis','ArtificialIntelligence','CyberSecurity','Network','Startup','TestStrategy']
b = [204,207,302,'B101',303,501,105]

dic = dict(zip(a,b))

n = int(input())
for _ in range(n):
    st = input()
    print(dic[st])