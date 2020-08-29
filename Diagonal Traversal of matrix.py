def diagonal(mat,n):
    for i in range(n-1,-1,-1):
        s=r=0
        h=i
        while h<n:
            s+=mat[r][h]
            r+=1
            h+=1
        print(s,end=' ')
    for j in range(1,n):
        s=h=0
        r=j
        while r<n:
            s+=mat[r][h]
            r+=1
            h+=1
        print(s,end=' ')        
t=int(input())
for i in range(t):
    n=int(input())
    mat=[]
    for i in range(n):
        a=list(map(int,input().split()))
        mat.append(a)
    diagonal(mat,n)
    print()
