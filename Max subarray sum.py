import sys
def maxsum(arr,n):
    maxofar=-sys.maxsize-1
    maxend=start=end=s=0
    for i in range(n):
        maxend+=arr[i]
        if maxofar<maxend:
            maxofar=maxend
            start=s
            end=i
        if maxend<0:
            maxend=0
            s=i+1
    return [maxofar,start,end]        
t=int(input())
for i in range(t):
    n=int(input())
    arr =list(map(int,input().strip().split(' ')))[:n]
    res=maxsum(arr,n)
    for val in res:
        print(val,end=' ')
    print()    
