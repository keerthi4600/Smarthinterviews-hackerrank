t=int(input())
for i in range(t):
    res=[]
    n=int(input())
    lst=list(map(int,input().split()))
    for i in range(1,n):
        val=lst[i]
        j=i-1
        while j>=0 and val <lst[j]:
            lst[j+1]=lst[j]
            j-=1
        res.append(j+1)
        lst[j+1]=val
    for ele in res:
        print(ele,end=' ')
    print()    
