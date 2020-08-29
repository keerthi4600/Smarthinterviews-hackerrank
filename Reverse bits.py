t=int(input())
for i in range(t):
    a=int(input())
    bina = bin(a)[2:]
    bina = bina[::-1]
    l=len(bina)
    res =''
    for i in range(32-l):
        res+='0'
    resu = bina+ res
    print(int(resu,2))
