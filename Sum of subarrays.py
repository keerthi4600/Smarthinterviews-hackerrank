n=int(input())
lst=list(map(int,input().strip().split(' ')))[:n]
res=[]
r=0
for i in range(n):
    r+=lst[i]
    res.append(r)    
#print(res)    
q=int(input())
for i in range(q):
    a,b=map(int,input().split(' '))
    print((res[b]-res[a])+lst[a])
