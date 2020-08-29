t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    count=0
    for j in range(n-1):
        for k in range(n-1):
            if lst[k]>lst[k+1]:
                lst[k],lst[k+1]=lst[k+1],lst[k]
                count+=1
    print(count)             
