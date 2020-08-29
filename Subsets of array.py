from itertools import combinations
def subset(arr):
    res=[]
    for i in range(1,n+1):
        p=list(combinations(arr,i))
        res.extend(p)
    res.sort()
    return res
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split(' ')))[:n]
    arr.sort()
    res=subset(arr)
    for ele in res:
        for val in ele:
            print(val,end=' ')
        print()    
    print()    
