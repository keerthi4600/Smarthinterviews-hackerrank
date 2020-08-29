def spiral(mat,i,j,r,n):    
    if i>=r or j>=n:
        return
    for g in range(i,n):
        print(mat[i][g],end=' ')
    for g in range(i+1,r):
        print(mat[g][r-1],end=' ')
    if r-1!=j:
        for g in range(n-2,j-1,-1):
            print(mat[r-1][g],end=' ')
    if n-1!=j:
        for g in range(r-2,i,-1):
            print(mat[g][j],end=' ')
    spiral(mat,i+1,j+1,r-1,n-1)
t=int(input())
for i in range(t):
    n=int(input())
    mat=[]
    for i in range(n):
        a=list(map(int,input().split()))
        mat.append(a)
    spiral(mat,0,0,n,n)
    print()
