t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    m=bin(x)[2:][::-1]
    n=bin(y)[2:][::-1]
    if x<y:
        m,n=n,m
    d=len(m)-len(n)
    n=n+d*'0'
    res=0
    for i in range(len(m)):
        if m[i]!=n[i]:
            res+=1
    print(res)
